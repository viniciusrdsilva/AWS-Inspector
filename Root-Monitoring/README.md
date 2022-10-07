# Root Monitor

Tool to create a bot that will runs every 3 minutes to identified if the Root account have been used.

You can get this information with CloudWatch and Trusted Advisor, but I've created it to study.

## Dependences:
  - AWS CLI configurated. You'll need to configurate the AWS CLI inserting a service account with permission to read, list and discribe in CloudTrail;
  - Slack Webhook. You need to change inserting the address of your webhook in the file [slack.py](#https://github.com/viniciusrdsilva/AWS-Inspector/root-monitor/src/slack/slack.py)

