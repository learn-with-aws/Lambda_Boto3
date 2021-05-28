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
    
    # Stop EC2 instances
    data.stop_instances(InstanceIds=instances_list)
    print ("The above instance got stopped")
    
    # Start Ec2 Instances
    #data.start_instances(InstanceIds=instances_list)
    #print ("The above instance got started")
