from pymongo import MongoClient
client =MongoClient("mongodb+srv://jayraj97:Jayraj%401906@nodeexpressprojects.db1swft.mongodb.net/?retryWrites=true&w=majority")
db = client["Vr-Wedding"]
demo=db["Vr-Wedding-Demo"]
refferal=db["Vr-Wedding-refferal"]
training=db["Vr-Wedding-training"]

