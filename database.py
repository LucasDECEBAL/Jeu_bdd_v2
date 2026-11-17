# Importer le client MongoDB
import os

from pymongo import MongoClient


def database_name():
    return os.environ.get("MONGODB_DB", "jeu_video")


def create_client():
    uri = os.environ.get("MONGODB_URI", "mongodb://127.0.0.1:27017/")
    return MongoClient(
        uri,
        connect=False,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000,
        socketTimeoutMS=5000,
    )