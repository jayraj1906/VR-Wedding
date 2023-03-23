from config.database import training
from bson.objectid import ObjectId
import json
import boto3

def get_all_training():
    data=[]
    document=training.find()
    for items in document:
        data.append(items)
    return str(data)

def get_a_training(id):
    document=training.find_one({"_id":ObjectId(id)})
    return str(document)

def create_training(data):
    data=dict(data)
    document=training.insert_one(data)
    client = boto3.client('lambda',region_name='us-east-1')
    subject="VR-Wedding Training"
    body=f"Name: {data['name']},Email: {data['email']} ,Mobile Number: {data['mobileNumber']} ,Profession: {data['profession']},City: {data['city']}"
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
    return f"Training created with id : {str(document.inserted_id)}"

def update_training(id,data):
    data=json.loads(data)
    training.update_one({"_id":ObjectId(id)},{"$set":data})
    return "training updated successfully"

def delete_training(id):
    training.update_one({"_id":ObjectId(id)},{"$set":{"isDeleted":True}})
    return "training has been deleted"