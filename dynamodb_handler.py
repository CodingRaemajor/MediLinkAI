import boto3
import uuid
from datetime import datetime

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('MediLinkPatients')

def save_patient_record(name, age, gender, symptoms, diagnosis):
    patient_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    item = {
        'patient_id': patient_id,
        'name': name,
        'age': int(age),
        'gender': gender,
        'symptoms': symptoms,
        'diagnosis': diagnosis,
        'timestamp': timestamp
    }

    table.put_item(Item=item)