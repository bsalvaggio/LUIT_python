#!/usr/bin/env python3
import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Create an SQS queue
queue_name = 'week15-sqs-queue'
response = sqs.create_queue(QueueName=queue_name)
queue_url = response['QueueUrl']
print('SQS queue created with URL:', queue_url)
