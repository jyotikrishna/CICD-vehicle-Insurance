import os
import sys
import certifi
import pymongo
from urllib.parse import quote_plus

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME


class MongoDBClient:
    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                username = os.getenv("MONGODB_USERNAME")
                password = os.getenv("MONGODB_PASSWORD")
                cluster_url = os.getenv("MONGODB_CLUSTER_URL")

                if username is None:
                    raise Exception("MONGODB_USERNAME is not set in bash")

                if password is None:
                    raise Exception("MONGODB_PASSWORD is not set in bash")

                if cluster_url is None:
                    raise Exception("MONGODB_CLUSTER_URL is not set in bash")

                username = quote_plus(username)
                password = quote_plus(password)

                mongo_db_url = (
                    f"mongodb+srv://{username}:{password}@{cluster_url}/"
                    f"?retryWrites=true&w=majority&appName=Cluster0"
                )

                ca = certifi.where()

                MongoDBClient.client = pymongo.MongoClient(
                    mongo_db_url,
                    tlsCAFile=ca
                )

                logging.info("MongoDB connection successful")

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

        except Exception as e:
            raise MyException(e, sys)