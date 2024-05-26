# pi-ai-msft

A Python-based AI platform for Pi Network using Azure Machine Learning for model training and Azure Functions for API services.

# Getting Started

To get started with the pi-ai-msft project, follow these steps:

## Clone the repository:

```
1. git clone https://github.com/KOSASIH/pi-ai-msft.git
```

## Create a virtual environment and install the required dependencies:

```
1. python -m venv venv
2..source venv/bin/activate
3. pip install -r requirements.txt
```

## Create an Azure Machine Learning workspace and configure the `config/azure_ml.config.json` file with your workspace details.

Create an Azure Functions app and configure the `config/azure_functions.config.json` file with your app details.

Run the `deploy.py` script to deploy the trained model as a web service.

## Directory Structure

The pi-ai-msft project has the following directory structure:

- config/: Configuration files for Azure Machine Learning and Azure Functions.
- data/: Datasets used for model training.
- models/: Trained machine learning models.
- azure_ml/: Azure Machine Learning scripts for model training and deployment.
- azure_functions/: Azure Functions scripts for API services.
- deploy.py: Script for deploying the trained model as a web service.
- requirements.txt: List of required dependencies.
