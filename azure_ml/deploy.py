from azureml.core.webservice import Webservice, AciWebservice
from azureml.core.model import InferenceConfig, Model
from azureml.core.environment import Environment

# Load model
model = Model(workspace=ws, name='model1')

# Define inference configuration
inference_config = InferenceConfig(runtime='python',
                                   entry_script='azure_functions/api.py',
                                   source_directory='.',
                                   environment=myenv)

# Define environment
myenv = Environment('pi-ai-env')
myenv.python.conda_dependencies = CondaDependencies.create(conda_packages=['scikit-learn==0.24.2'],
                                                            pip_packages=['azureml-core', 'azureml-mlflow', 'inference-schema[numpy-support]'])

# Create web service
aci_service = Webservice(workspace=ws,
                         name='pi-ai-service',
                         inference_config=inference_config,
                         models=[model],
                         create_new_model=False)

# Deploy web service
aci_service.deploy()
