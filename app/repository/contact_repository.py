""" """
from pymongo import MongoClient
from urllib.parse import quote_plus
from bson.json_util import loads, dumps
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
            password=None
    ):
        self.scheme = "mongodb://"  # scheme or os.getenv("DB_SCHEME")
        self.host = "localhost"  # host or os.getenv("DB_HOST")
        self.db_name = "Projects"  # db_name or os.getenv("DB_NAME")
        self.collection_name = "AddressBookAppDB"  # collection_name or os.getenv("DB_COLLECTION")
        self.user_name = ""  # user_name or os.getenv("DB_USERNAME")
        self.password = ""  # password or os.getenv("DB_PASSWORD")

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
        res = self.collection.insert_one(data)
        print("res : ", res.__class__)

    def read(self, name):
        """ """
        query = {"name": name}
        res = self.collection.find_one(query)
        #return dumps(res)
        return res

    def delete(self, name):
        query = {"name": name}
        res = self.collection.delete_one(query)

