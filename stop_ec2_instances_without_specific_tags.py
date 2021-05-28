
## Stop the Server if they don't have any tags.

#### Steps - Create a Lambda and setup a cloudwatch event pattren. Select EC2 service type and event.

import json
import boto3
data = boto3.client('ec2')
def lambda_handler(event, context):
    instances = data.describe_instances(Filters=[{'Name': 'tag:env', 'Values': ['wc_testserver']}])
    instances_list = []
    for instance in instances['Reservations']:
        for instance_id in instance['Instances']:
            instances_list.append(instance_id['InstanceId'])
    print (instances_list)
    data.stop_instances(InstanceIds=instances_list)
    #data.stop_instances(InstanceIds=instances_list)
    print ("The above instance got start")
