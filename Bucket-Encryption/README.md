# Public Buckets

Tool to check if there are buckets wihtout enabled encryption in your environment.


## Dependences:
  - AWS CLI configurated. You'll need to configurate the AWS CLI inserting a service account with permission to read, list and discribe in CloudTrail;

## Optional:
  - Except Bucket List: Here you can pass a List of bucket that the tool won't scan, it would help you to don't get alarm in buckets that need to be in fact public. Just pass the List in [bucket-encryption.py](https://github.com/viniciusrdsilva/AWS-Inspector/blob/main/Bucket-Encryption/bucket-encryption.py) file;

