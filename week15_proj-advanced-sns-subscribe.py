import boto3

sns = boto3.client('sns', region_name='<your_region>')
topic_arn = '<your_topic_arn>'

response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='<your_email_address>',
)

subscription_arn = response['SubscriptionArn']
print('Subscription ARN:', subscription_arn)
