from pymongo import MongoClient
import constants as constant

__url__=f"mongodb+srv://{constant.USERNAME}:{constant.PASSWORD}@{constant.DB_HOST}/?retryWrites=true&w=majority"

_client = MongoClient(__url__)
db = _client[constant.DATABASE]

employeeCollection = db[constant.EMPLOYEE]
roleCollection = db[constant.ROLES]
orgCollection = db[constant.ORGANISATION]




