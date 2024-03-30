import os
import urllib.request as request
import zipfile
#from src.mlProject import logger
from src.mlProject.utils.common import get_size
#import logging  # Importing logging module directly
from src.mlProject.logging import *
from src.mlProject.constants import *
from src.mlProject.entity.config_entity import *
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        print(data.columns)

        # Remove 'Id' column if it exists
        data = self.remove_id_column(data)
        
        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

    def remove_id_column(self, data):
        if 'Id' in data.columns:
            data.drop(['Id'], inplace=True, axis=1)
            logger.info("Removed 'Id' column from the dataset")
        else:
            logger.info("No 'Id' column found in the dataset. Skipping removal.")
        return data

