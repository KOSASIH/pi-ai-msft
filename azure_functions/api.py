import azure.functions as func
from azureml.core import Workspace, Model

# Create Azure ML workspace
ws = Workspace.from_config()

# Load model
model = Model(ws, 'model1')

# Create API function
def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get input data from request
    input_data = req.get_json()

    # Make prediction using model
    output = model.predict(input_data)

    # Return response
    return func.HttpResponse(body=output, status_code=200)
