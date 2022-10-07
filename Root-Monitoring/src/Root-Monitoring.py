import datetime
from time import sleep
import boto3
from slack.slack import send_alert


# Creating variables
start = datetime.datetime.now()
lastRun = datetime.datetime.now()


# Connection with CloudTrail
client = boto3.Session().client('cloudtrail')

while True:
    start = datetime.datetime.now()
    now = start
    print(f'agora = {start}')
    print(f'lasrun = {lastRun}')
    response = client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'Username',
                'AttributeValue': 'root'
            },
        ],
        StartTime=lastRun,
        EndTime=now,
        MaxResults=1
    )

    if response["Events"]:
        send_alert()
    lastRun = now
    sleep(180)