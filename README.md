# NextGenAI Agents Workshop

Welcome to the repository dedicated to the **Agent to Agent and Agent to Tool: Building Next Gen Reasoning Systems on Azure** workshop!

This repository contains code samples and instructions to help you go through the workshop exercises.

## Prerequisites

### Sign into the Azure AI Foundry portal

1. Open a browser window and navigate to the [Azure AI Foundry portal](https://ai.azure.com/).

    ![Azure AI Foundry portal](./media/ex00-aifoundry-portal.png)

2. Sign in with your Azure account credentials. The user name should be `fllm-labuser-NN@foundationallm.ai`, where `NN` is your assigned number during the workshop. The password will also be provided during the workshop.

>[!IMPORTANT]
>You will be asked to provide additional settings to keep the >account secure. Please make sure you skip the multi-factor >authentication (MFA) setup, as this is not supported in the >workshop environment.

3. Select `Next` on the `Let's keep your account secure` page.

    ![Keep your account secure](./media/ex00-keep-account-secure.png)

    Select `Skip setup`.

    ![Skip setup](./media/ex00-skip-setup.png)

4. After signing in, you will be presented with the list of Azure AI Foundry projects. Select the project named `project-NN`, where `NN` is your assigned number during the workshop.

    ![Select project](./media/ex00-select-project.png)

>[!IMPORTANT]
Your account has the required access only to the `project-NN` project. Please make sure you select the correct project, otherwise you will see multiple permissions errors and will not be able to complete the exercises.

5. After selecting the project, you are ready to start using Azure AI Foundry.

   ![AI Foundry project](./media/ex00-aifoundry-project.png)

### Set up your local environment (optional)

**Requirements:**

- Visual Studio Code (download [here](https://code.visualstudio.com/)). Make sure to install the `Python` and `Python Debugger` extensions for Visual Studio Code (search for "Python" and "Python Debugger" in the Extensions view and install the ones published by Microsoft).
- Python 3.11 or later (download [here](https://www.python.org/downloads/)).
- Azure CLI 2.77.0 (download [here](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)).

Once you have installed the prerequisites, follow these steps to set up your local environment:

1. Clone this repository to your local machine and open it in Visual Studio Code. You can use the following command in your terminal (make sure to run it in the directory where you want to clone the repository):

    ```cmd
    git clone https://github.com/foundationallm/nextgenai-agents-workshop NextGenAI-Agents-Workshop
    ```

2. In Visual Studio Code, select `CTRL+SHIFT+P` (or `CMD+SHIFT+P` on Mac) to open the command palette, then type `Python: Create Environment` and select it. When prompted, select `Venv` as the environment type and `Python 3.11` (or above) as the base interpreter. When prompted to select dependencies to install, select `requirements.txt` and then select `OK`. This will trigger the creation of a new Python virtual environment named `.venv` and install the required dependencies. The process may take a few minutes and the progress will be shown in a popup in the bottom right corner of Visual Studio Code (you can select `Show logs` if want to see more details).

    If you prefer to create the virtual environment manually, you can do so by following these steps:
    - Open the Powershell terminal in Visual Studio Code (View > Terminal) and create a new Python virtual environment by running the following command (if it's a PowerShell terminal):

        ```pwsh
        & 'C:\Program Files\Python311\python.exe' -m venv .venv
        ```

        Make sure to adjust the path to `python.exe` if your Python installation is in a different location.

    - Once your virtual environment is created, activate it by running the following command:

        ```pwsh
        .\.venv\Scripts\activate
        ```

    - Install the required dependencies by running the following command:

        ```pwsh
        pip install -r requirements.txt
        ```

## Exercise 1: Create a simple agent (witty cat) in AI Foundry ##



## Exercise 2: Create a simple agent (Fibonacci sequence) with Python and AI Foundry ##

This exercise is a code-only exercise. Before starting the exercise, please make sure you have completed the [Prerequisites](#prerequisites) section (including the optional [Setup your local environment](#set-up-your-local-environment-optional)).

Run [first_agent.py](./first-agent.py).

## Exercise 3: Create an agent with Code Interpreter in AI Foundry ##

## Exercise 4: Create an agent with Code Interpreter with Python and AI Foundry ##

This exercise is a code-only exercise. Before starting the exercise, please make sure you have completed the [Prerequisites](#prerequisites) section (including the optional [Setup your local environment](#set-up-your-local-environment-optional)).

Run [agent-code-interpreter.py](./agent-code-interpreter.py).

## Exercise 5: Create an agent with Azure REST API Specs MCP tool with Python and AI Foundry ##

This exercise is a code-only exercise. Before starting the exercise, please make sure you have completed the [Prerequisites](#prerequisites) section (including the optional [Setup your local environment](#set-up-your-local-environment-optional)).

Run [agent-mcp.py](./agent-mcp.py).

## Exercise 6: Create an agent with MS Learn MCP tool with Python and AI Foundry ##

This exercise is a code-only exercise. Before starting the exercise, please make sure you have completed the [Prerequisites](#prerequisites) section (including the optional [Setup your local environment](#set-up-your-local-environment-optional)).

Run [agent-mcp-mslearn.py](./agent-mcp-mslearn.py).

## Exercise 7: Create an agent (weather) with OpenAPI tools in AI Foundry ##

## Exercise 8: Create an agent (holidays) with OpenAPI tool with Python and AI Foundry ##

This exercise is a code-only exercise. Before starting the exercise, please make sure you have completed the [Prerequisites](#prerequisites) section (including the optional [Setup your local environment](#set-up-your-local-environment-optional)).

Run [agent-openapi-holidays.py](./agent-openapi-holidays.py).

## Exercise 9: Create an agent (bing search) with AI Foundry ##

## Exercise 10: Create an agent (bing custom search) with AI Foundry ##

## Exercise 11: Create an agent (bing custom search) with AI Foundry and Python ##

This exercise is a code-only exercise. Before starting the exercise, please make sure you have completed the [Prerequisites](#prerequisites) section (including the optional [Setup your local environment](#set-up-your-local-environment-optional)).

Run [agent-tech-search.py](./agent-tech-search.py).

## Exercise 12: Creating an agent with Fabric Data Agent in AI Foundry ##

## Exercise 13: Create connected agents in AI Foundry ##