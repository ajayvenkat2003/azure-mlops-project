import pandas as pd
from sklearn.linear_model import LogisticRegression
import mltable
import argparse
import mlflow

class TrainModel:
    def __init__(self,data_asset,model):
        self.data_asset = data_asset
        self.model = model
    def load_data(self):
        self.data = mltable.load(self.data_asset).to_pandas_dataframe()
        print("data loaded..")
    def preprocess_data(self):
        self.data = self.data.dropna()
        print("data preprocessed...")
    def train_model(self):
        target = self.data.pop("Diabetic")
        print("model training started..")
        self.model.fit(self.data,target)
        print("model trained..")
        with mlflow.start_run() as run:
            mlflow.sklearn.log_model(self.model,artifact_path="logistic_model")
            model = mlflow.register_model(f"runs:/{run.info.run_id}/logistic_model",name="logistic_model")
        client = mlflow.MlflowClient()
        client.set_registered_model_alias(model.name,"latest",model.version)
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file",default="path to file")
    args = parser.parse_args()
    print(args)
    train = TrainModel(args.file,LogisticRegression())
    train.load_data()
    train.preprocess_data()
    train.train_model()
    
