import boto3
import json

secret_name = "dev/ocp"
region_name = "us-east-1"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

get_secret_value_response = client.get_secret_value(SecretId=secret_name)

secret = get_secret_value_response['SecretString']

dictData = json.loads(secret)
#print(dictData)
print(dictData['host'])
print(dictData['port'])
