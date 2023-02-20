import boto3

# Set the region where your instances are located
region = 'us-east-1'

# Create an EC2 client object for the specified region
ec2_client = boto3.client('ec2', region_name=region)

# Retrieve a list of running instances with the Environment: Dev tag
instances = ec2_client.describe_instances(Filters=[
    {'Name': 'tag:Environment', 'Values': ['Dev']},
    {'Name': 'instance-state-name', 'Values': ['running']}
])

# Extract the instance IDs from the filtered results and store them in a list
instance_ids = [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]

# If there are running instances with the Environment: Dev tag, stop them
if len(instance_ids) > 0:
    ec2_client.stop_instances(InstanceIds=instance_ids)
    print(f'Successfully stopped {len(instance_ids)} instances: {instance_ids}')
else:
    print('No instances to stop')
