import pymongo
import certifi
from pymongo import MongoClient

client = MongoClient("mongodb+srv://selinahrdz:Sh760558@cluster0.ugzphul.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true",tlsCAFile=certifi.where())
db = client['Projects']
collection = db['Project1']
document = {'Name': 'P1', 'ID': 'as1234', 'Description': 'This is the first project'}
collection.insert_one(document)
client.close()



