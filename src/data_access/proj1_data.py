import sys 
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:
    """
    A Class to export MongoDB records as a pandas DataFrame.
    """

    def __init__(self) -> None: 
        """
        Initialized the MongoDB Client Connection
        """
        try:
            self.mongo_client = MongoDBClient(database_name = DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys) 

    def export_collection_as_dataframe(self, collection_name: str , database_name:Optional[str] = None) -> pd.DataFrame:
        """
        Export entire MongoDB collection as a pandas DataFrame.

        Parameters:
        -----------
        collection_name : str, optional 
            Name of the MongoDB collection to export. Defaults to DATABASE_NAME.
        database_name : Optional[str], optional 
            Name of the database to connect to. If None, uses default DATABASE_NAME, by default None

        Raises:
        -------
        MyException 
            If there is an issue exporting data from MongoDB.

        Returns:
        ------
        pd.DataFrame 
            DataFrame containing the exported data.
        
        """
        try: 
            #Access specified collection from the default or specified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
                
            ##Convert collection data to dataframe and preprocess
            print("Fetching data from mongodb")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fetched with len: {len(df)}")
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"])
            df.replace({"na" :np.nan}, inplace= True)
            return df 
        except Exception as e:
            raise MyException(e, sys)