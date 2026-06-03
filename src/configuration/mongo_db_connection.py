import os
import  sys
import pymongo 
import certifi 

from src.exception import MyException
from src.logger import logging 
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

##Loading the certificate authority file to avoid timweout errors when connecting to MomgoDB 
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the MongoDB Database.
    Attributes:
    client :MongoClient
    A shared Mngoclient instance for the class.
    database: database 
    The specific database instance that MongoDBClient connects to.
    
    Methods :
    __init__(database_name: str) ->None
    Initializes the MongoDB connection using the given database name.

    """
    client = None ##Shared MongoClient instance for the class

    def __init__(self, database_name: str= DATABASE_NAME)->None:
       """
       Initializes a connection to the MongoDB Database. If no exisiting connection is found , it establishes a new one.
       
       Parameters:
       database_name : str, optional 
       Name of the MongoDB database to connect to. default is set by DATABASE_NAME constant.

       Raises:
       MyException
       If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
       """
       try :
        ##Check if a Mongodb client connection has already been establishes; if not, create a new one
        if MongoDBClient.client is None:
            mongo_db_url = os.getenv(MONGODB_URL_KEY) ##Retreive MongoDB URL from environemnt variables
            if mongo_db_url is None:
                raise Exception(f"Environment Variable '{MONGODB_URL_KEY}' is not set")

            ##Establish a new MongoDB Client connection 
            MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            ##Use the shared Mongoclient for this instance 
            self.client = MongoDBClient.client 
            self.database = self.client[database_name] ##Connect to the specified database
            self.database_name = database_name
            logging.info("MongoDB connection established successfully")
       except Exception as e:
            ##Raise a custom exception if traceback details if connection fails
            raise MyException (e, sys) 
            
    
    

        