import boto3
import pprint
import sys
from botocore.exceptions import ClientError
ec2 = boto3.resource('ec2')
ls=['t2.micro','t2.small','t2.medium','t2.large']
print("Enter the instance type")
var = input()

client = boto3.client('ec2')
response = client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance["InstanceType"] == var:

        # This sample print will output entire Dictionary object
        # This will print will output the value of the Dictionary key 'InstanceId'
            print(instance["InstanceId"], instance["InstanceType"])
