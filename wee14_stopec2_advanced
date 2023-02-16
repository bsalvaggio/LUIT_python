import boto3

# Create an EC2 client object for us-east-1 region
ec2 = boto3.client('ec2', region_name='us-east-1')

# Function to check if an instance is tagged as "Environment:Dev"
def is_dev(instance):
    tag = {'Key':'Environment', 'Value':'Dev'}
    is_dev = False
    # Check if the instance has the "Environment:Dev" tag
    if tag in instance['Tags']:
        is_dev = True
    return is_dev

# Function to check if an instance is in "running" state
def is_running(instance):
    is_running = False
    # Check if the instance is in "running" state
    if instance['State']['Name'] == 'running':
        is_running = True
    return is_running

# Retrieve information about all instances in the region
instance_attr = ec2.describe_instances() 

# Get the list of reservations
reservations = instance_attr["Reservations"] 

# Loop through all instances and stop the instances that meet the criteria
for reservation in reservations: 
    for instance in reservation["Instances"]: 
        if (is_dev(instance) and is_running(instance)): 
            instance_id = instance['InstanceId'] 
            ec2.stop_instances(InstanceIds=[instance_id]) 
            print("The following instance has stopped: " + instance_id)
