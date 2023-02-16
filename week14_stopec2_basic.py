import boto3

# create EC2 client
ec2 = boto3.client('ec2')

# get all running instances
instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])['Reservations']

# stop all running instances
for instance in instances:
    for i in instance['Instances']:
        instance_id = i['InstanceId']
        ec2.stop_instances(InstanceIds=[instance_id])
        print('Stopped instance: ', instance_id)
