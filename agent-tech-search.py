import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import BingCustomSearchTool
from dotenv import load_dotenv
load_dotenv()

# Create an Azure AI Client from an endpoint, copied from your Azure AI Foundry project.
# You need to login to Azure subscription via Azure CLI and set the environment variables
# Ensure the PROJECT_ENDPOINT environment variable is set
project_endpoint = os.environ["PROJECT_ENDPOINT"]  

# Create an AIProjectClient instance
project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)

bing_custom_connection = project_client.connections.get(name=os.environ["BING_CUSTOM_CONNECTION_NAME"])
conn_id = bing_custom_connection.id

print(conn_id)

configuration_name = os.environ["BING_CUSTOM_INSTANCE_NAME"]
# Initialize Bing Custom Search tool with connection id and configuration name
bing_custom_tool = BingCustomSearchTool(connection_id=conn_id, instance_name=configuration_name)

# Create agent with the bing custom search tool and process assistant run
with project_client:
    agents_client = project_client.agents

    agent = agents_client.create_agent(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        name="my-agent",
        instructions="You are a helpful agent",
        tools=bing_custom_tool.definitions,
    )
    print(f"Created agent, ID: {agent.id}")

    # Create thread for communication
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Create message to thread
    message = agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What new ChatGPT feature did OpenAI launch?",
    )
    print(f"Created message, ID: {message.id}")

    # Create and process Agent run in thread with tools
    run = agents_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
    print(f"Run finished with status: {run.status}")

    if run.status == "failed":
        print(f"Run failed: {run.last_error}")

    # print the bing search query (to be compliant with terms of service)
    urls = []
    for step in project_client.agents.run_steps.list(run_id=run.id, thread_id=thread.id):
        step_details = step['step_details'] if isinstance(step, dict) else getattr(step, 'step_details', None)
        if step_details.get('type') != 'tool_calls':
            continue
        for tc in step_details.get('tool_calls', []):
            if tc.get('type') == 'bing_custom_search':
                url = tc.get('bing_custom_search', {}).get('requesturl')
                if url:
                    urls.append(url)
    print(f"bing search url: {urls}")

    # Fetch and log all messages
    messages = agents_client.messages.list(thread_id=thread.id)
    for msg in messages:
        if msg.text_messages:
            for text_message in msg.text_messages:
                print(f"Agent response: {text_message.text.value}")
            for annotation in msg.url_citation_annotations:
                print(f"URL Citation: [{annotation.url_citation.title}]({annotation.url_citation.url})")

            