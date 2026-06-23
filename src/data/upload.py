import mltable
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient
from azure.ai.ml.entities  import Data
from azure.identity import DefaultAzureCredential
import yaml
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--env",default="DEV")
parser.add_argument("--file",default="./data/diabetes-data")
parser.add_argument("--name",default="train-data")
args = parser.parse_args()
ENV = args.env
LOCATION = args.file
NAME = args.name
credential = DefaultAzureCredential()
with open('./configs/infra.yaml',"r+") as file:
    configs = yaml.safe_load(file)
SUBSCRIPTION_ID = configs[ENV]["SUBSCRIPTION_ID"]
WORKSPACE_NAME = configs[ENV]["WORKSPACE_NAME"]
RESOURCE_GROUP_NAME= configs[ENV]["RESOURCE_GROUP_NAME"]
ml_client = MLClient(credential,resource_group_name=RESOURCE_GROUP_NAME,subscription_id=SUBSCRIPTION_ID,workspace_name=WORKSPACE_NAME)
data = Data(path=LOCATION,type=AssetTypes.MLTABLE,name=NAME,version="1")
ml_client.data.create_or_update(data)