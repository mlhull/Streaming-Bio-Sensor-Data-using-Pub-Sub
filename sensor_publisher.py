import os
from google.cloud import pubsub_v1
import random
import json
import time
from dotenv import load_dotenv
import datetime

# Load environment variables, this sets GOOGLE_APPLICATION_CREDENTIALS to service acct w/ pub/sub role on project
load_dotenv()
topic_path = os.environ.get('TOPIC_PATH')

# Connect to pub/sub client
publisher = pubsub_v1.PublisherClient()

def random_resp_entry():
    return {
        'timestamp': str(datetime.datetime.now()),
        'measure': random.choice(['RESPIRATORY_RATE']), 
        'message': str(random.randint(12,44)),
        'user_id': random.randint(1000, 9999),
    }

def random_hr_entry():
    return {
        'timestamp': str(datetime.datetime.now()),
        'measure': random.choice(['HEART_RATE']), 
        'message': str(random.randint(40, 100)),
        'user_id': random.randint(1000, 9999),
    }

def random_steps_entry():
    return {
        'timestamp': str(datetime.datetime.now()),
        'measure': random.choice(['STEPS_TAKEN']), 
        'message': str(random.randint(0,155)),
        'user_id': random.randint(1000, 9999),
    }

# Every 5 seconds, loop through the 3 types of logs randomly, convert to message and publish to topic
while True:
    chosen_function = random.choice([random_resp_entry, random_hr_entry, random_steps_entry])
    data = chosen_function()

    message = json.dumps(data).encode('utf-8')

    future = publisher.publish(topic_path, message)
    print("published message id", future.result())
    print(data)

    time.sleep(5)