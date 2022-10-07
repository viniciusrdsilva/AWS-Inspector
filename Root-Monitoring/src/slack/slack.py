import json
import requests


slack_channel = 'https://webhook'



def send_alert():
    """
    This Function create a standard the information that will be sended to slack. And will send it.
    """
    
    body_message = []
    body_message.append({
        "color": "#cc0000",
        "text": "Para mais informações clique <https://us-east-1.console.aws.amazon.com/cloudtrail/home?region=us-east-1#/events?Username=root|AQUI>.",
    })

    message = {
        "text": ":alert:   *New access identified with root account in AWS*   :alert:",
        "attachments": body_message
    }
    
    SLACK_WEBHOOK_URL = slack_channel
    requests.post(SLACK_WEBHOOK_URL, data=json.dumps(message))


