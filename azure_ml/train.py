from azureml.core import Workspace, Experiment, ScriptRunConfig
from azureml.core.compute import AmlCompute
from azureml.core.runconfig import RunConfiguration

# Create Azure ML workspace
ws = Workspace.from_config()

# Create experiment
experiment = Experiment(ws, 'pi-ai-msft')

# Create compute target
compute_target = AmlCompute(ws, 'cpu-cluster')

# Create run configuration
run_config = RunConfiguration()
run_config.target = compute_target

# Create script run config
script_run_config = ScriptRunConfig(source_directory='.', script='train.py', run_config=run_config)

# Submit experiment
experiment.submit(config=script_run_config)
