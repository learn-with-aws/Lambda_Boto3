from __future__ import print_function

import boto3
import time

def lambda_handler(event, context):
    path = []
    for items in event["Records"]:
        if items["s3"]["object"]["key"] == "index.html":
            path.append("/")
        else:
            path.append("/" + items["s3"]["object"]["key"])
    print(path)
    client = boto3.client('cloudfront')
    invalidation = client.create_invalidation(DistributionId='EORGUSGVF3IGK',
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': path
        },
        'CallerReference': str(time.time())
    })
