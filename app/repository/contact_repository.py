""" """
from pymongo import MongoClient
from urllib.parse import quote_plus
import os

_CLIENTS = {}


class ContactRepository:
    """ """

    def __init__(
            self,
            scheme=None,
            host=None,
            db_name=None,
            user_name=None,
            password=None,
            collection_name=None
    ):
        self.scheme = "mongodb://" or scheme or os.getenv("DB_SCHEME")
        self.host = "localhost" or host or os.getenv("DB_HOST")
        self.db_name = "Projects" or db_name or os.getenv("DB_NAME")
        self.collection_name = "AddressBookAppDB" or collection_name or os.getenv("DB_COLLECTION")
        self.user_name = "" or user_name or os.getenv("DB_USERNAME")
        self.password = "" or password or os.getenv("DB_PASSWORD")

        if user_name and password:
            username = quote_plus(user_name)
            password = quote_plus(password)
            uri = f"{self.scheme}{username}:{password}@{self.host}"
        else:
            uri = f"{self.scheme}{self.host}"

        self._client = MongoClient(uri)
        self._db = self._client["Projects"]
        self.collection = self._db["AddressBookAppDB"]

    def create(self, data):
        """ """
        if data is None:
            raise ValueError("data is None")
        self.collection.insert_one(data)

    def read(self, name):
        """ """
        query = {"name": name}
        return self.collection.find_one(query)

    def delete(self, name):
        query = {"name": name}
        self.collection.delete_one(query)

    def update(self, name, data):
        where = {"name": name}
        update = {"$set": data}
        self.collection.update_one(where, update)

