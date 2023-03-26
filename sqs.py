import boto3


# Create an Amazon SQS client
sqs = boto3.client('sqs')


# Create a queue
response = sqs.create_queue(QueueName='MyQueue')
url = sqs.get_queue_url(QueueName='MyQueue')


# Send a message to the queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Hello World'
)

# Receive a message from the queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

print(response)


