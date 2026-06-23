#!/bin/bash

# Define variables (NO spaces around '=')
COMPUTE_INSTANCE="aml-compute"
REGION="eastus"
SUBSCRIPTION="17d9af06-ef0a-4411-878f-2198e61bfd65"

# Dev Environment
DEV_RESOURCE_GROUP_NAME="dev-env-group"
DEV_WORKSPACE_NAME="dev-env-workspace"

# Test Environment
TEST_RESOURCE_GROUP_NAME="test-env-group"
TEST_WORKSPACE_NAME="test-env-workspace"

# Prod Environment
PROD_RESOURCE_GROUP_NAME="prod-env-group"
PROD_WORKSPACE_NAME="prod-env-workspace"


# --- SET UP DEV ENVIRONMENT ---
echo "Setting up dev environment..."
az group create --name $DEV_RESOURCE_GROUP_NAME --location $REGION --subscription $SUBSCRIPTION
echo "Group $DEV_RESOURCE_GROUP_NAME created..."

az ml workspace create --name $DEV_WORKSPACE_NAME --resource-group $DEV_RESOURCE_GROUP_NAME --subscription $SUBSCRIPTION
echo "Workspace $DEV_WORKSPACE_NAME created..."

# Created compute by explicitly providing group and workspace context
az ml compute create --name $COMPUTE_INSTANCE --size STANDARD_DS11_V2 --type ComputeInstance --resource-group $DEV_RESOURCE_GROUP_NAME --workspace-name $DEV_WORKSPACE_NAME --subscription $SUBSCRIPTION
echo "Dev compute instance created..."


# --- SET UP TEST ENVIRONMENT ---
echo "Setting up test environment..."
az group create --name $TEST_RESOURCE_GROUP_NAME --location $REGION --subscription $SUBSCRIPTION
echo "Group $TEST_RESOURCE_GROUP_NAME created..."

az ml workspace create --name $TEST_WORKSPACE_NAME --resource-group $TEST_RESOURCE_GROUP_NAME --subscription $SUBSCRIPTION
echo "Workspace $TEST_WORKSPACE_NAME created..."

az ml compute create --name $COMPUTE_INSTANCE --size STANDARD_DS11_V2 --type ComputeInstance --resource-group $TEST_RESOURCE_GROUP_NAME --workspace-name $TEST_WORKSPACE_NAME --subscription $SUBSCRIPTION
echo "Test compute instance created..."


# --- SET UP PROD ENVIRONMENT ---
echo "Setting up prod environment..."
az group create --name $PROD_RESOURCE_GROUP_NAME --location $REGION --subscription $SUBSCRIPTION
echo "Group $PROD_RESOURCE_GROUP_NAME created..."

az ml workspace create --name $PROD_WORKSPACE_NAME --resource-group $PROD_RESOURCE_GROUP_NAME --subscription $SUBSCRIPTION
echo "Workspace $PROD_WORKSPACE_NAME created..."

az ml compute create --name $COMPUTE_INSTANCE --size STANDARD_DS11_V2 --type ComputeInstance --resource-group $PROD_RESOURCE_GROUP_NAME --workspace-name $PROD_WORKSPACE_NAME --subscription $SUBSCRIPTION
echo "Prod compute instance created..."