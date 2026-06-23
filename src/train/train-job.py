import mltable
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient,command,Input
from azure.ai.ml.entities  import Data
from azure.identity import DefaultAzureCredential
import yaml

ENV = "DEV"
credential = DefaultAzureCredential()
with open('./configs/infra.yaml',"r+") as file:
    configs = yaml.safe_load(file)
SUBSCRIPTION_ID = configs[ENV]["SUBSCRIPTION_ID"]
WORKSPACE_NAME = configs[ENV]["WORKSPACE_NAME"]
RESOURCE_GROUP_NAME= configs[ENV]["RESOURCE_GROUP_NAME"]
ml_client = MLClient(credential,resource_group_name=RESOURCE_GROUP_NAME,subscription_id=SUBSCRIPTION_ID,workspace_name=WORKSPACE_NAME)
data_input = Input(path="azureml:train-data:1")
train_job =  command(
name="train-job6",
display_name="training",
experiment_name="training_exp",
inputs={"data_asset":data_input },
code="./",
command = "python src/train/train.py --file ${{inputs.data_asset}}",
environment="my-env:6",
compute="aml-compute"
)
ml_client.jobs.create_or_update(train_job)