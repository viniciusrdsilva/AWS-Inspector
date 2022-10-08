# Public Buckets

Tool to check if there are public buckets in your environment.

I create this tool based in [s3-inpector](https://github.com/clario-tech/s3-inspector).

## Dependences:
  - AWS CLI configurated. You'll need to configurate the AWS CLI inserting a service account with permission to read, list and discribe in CloudTrail;

## Optional:
  - Except Bucket List: Here you can pass a List of bucket that the tool won't scan, it would help you to don't get alarm in buckets that need to be in fact public. Just pass the List in [public-buckets.py](https://github.com/viniciusrdsilva/AWS-Inspector/blob/main/Public-buckets/public-buckets.py) file;

