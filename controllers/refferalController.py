from config.database import refferal
from bson.objectid import ObjectId
import json
import boto3

def get_all_refferal():
    data=[]
    document=refferal.find()
    for items in document:
        data.append(items)
    return str(data)

def get_a_refferal(id):
    document=refferal.find_one({"_id":ObjectId(id)})
    return str(document)

def create_refferal(data):
    data=dict(data)
    document=refferal.insert_one(data)
    client = boto3.client('lambda',region_name='us-east-1')
    subject="VR-Wedding Refferal"
    body=f"Mobile Number: {data['mobileNumber']}"
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
    return str(document.inserted_id)

def update_refferal(id,profession,name,city):
    # data=json.loads(data)
    refferal.update_one({"_id":ObjectId(id)},{"$set":{"profession":profession,"name":name,"city":city}})
    return "Refferal updated successfully"

def delete_refferal(id):
    refferal.update_one({"_id":ObjectId(id)},{"$set":{"isDeleted":True}})
    return "Refferal has been deleted"