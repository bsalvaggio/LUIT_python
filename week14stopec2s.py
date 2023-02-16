#!/usr/bin/env python3

import boto3
import requests

# Get the instance ID of the running instance
response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
instance_id = response.text

# Use the EC2 resource and get all instances
ec2 = boto3.resource('ec2')
instances = ec2.instances.all()

# Loop through the instances and stop them if they are not the current instance and are running
for instance in instances:
    if instance.id != instance_id and instance.state['Name'] == 'running':
        response = instance.stop()
        print(f'Stopped instance: {instance.id}')