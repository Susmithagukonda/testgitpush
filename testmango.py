'''import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = "mongodb+srv://gukondasusmitha:Susmitha#02@cluster0.ofvxmrg.mongodb.net/?retryWrites=true&w=majority"


db = client.test
print(db)'''

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gukondasusmitha:Susmitha#02@cluster0.ofvxmrg.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.test
print(db)

d={"name":"susmitha","surname":"gukonda","email":"susmitha@gamil.com"}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
