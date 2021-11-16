import boto3
import api_secrets as sec

class DynamoLogger(object):

    def __init__(self):
        self.client = boto3.client('dynamodb', aws_access_key_id=sec.aws_access, aws_secret_access_key=sec.aws_secret, region_name='us-east-2')