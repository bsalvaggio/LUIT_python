#!/usr/bin/env python3

import boto3

sns = boto3.client('sns', region_name='<us-east-1>')

response = sns.create_topic(Name='<week15_sns>')
topic_arn = response['TopicArn']
print('Topic ARN:', topic_arn)
