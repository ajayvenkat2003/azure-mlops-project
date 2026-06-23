import mltable
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient,command,Input
from azure.ai.ml.entities  import Data,Environment,BuildContext
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
env = Environment(
    name="my-env",
    version="6",
    description="This is for running jobs",
    build=BuildContext(path="./")
)
ml_client.environments.create_or_update(env)