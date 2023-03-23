from config.database import demo
from bson.objectid import ObjectId
import json
import boto3

def get_all_demo():
    data=[]
    document=demo.find()
    for items in document:
        data.append(items)
    return str(data)

def get_a_demo(id):
    document=demo.find_one({"_id":ObjectId(id)})
    return str(document)

def create_demo(data):
    data=dict(data)
    demo.insert_one(data)
    client = boto3.client('lambda',region_name='us-east-1')
    subject="VR-Wedding Demo"
    #Budget:str Country:str  Message:str
    body=f"Name: {data['name']}, Email: {data['email']}, Mobile Number: {data['mobileNumber']}, Profession: {data['profession']}, City: {data['city']}, Country: {data['country']}, Wedding status: {data['weddingStatus']}, Month: {data['month']}, Budget: {data['budget']}, Message: {data['message']}"
    inputData={
        "Subject": subject,
        "Body": body,
        "To": "gewgawrav@gmail.com"
    }
    payload = json.dumps(inputData).encode('utf-8')
    response = client.invoke(
        FunctionName='SendEmailFunc',
        Payload=payload,
        InvocationType='RequestResponse'
    )
    output = response['Payload'].read().decode('utf-8')
    return "Demo created successfully"

def update_demo(id,data):
    data=json.loads(data)
    demo.update_one({"_id":ObjectId(id)},{"$set":data})
    return "Demo updated successfully"

def delete_demo(id):
    demo.update_one({"_id":ObjectId(id)},{"$set":{"isDeleted":True}})
    return "Demo has been deleted"