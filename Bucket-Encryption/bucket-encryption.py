import boto3
import termcolor
from src.get_encryption import get_buckets_without_encryption



# Creating variables
EXCEPTION_BUCKET_LIST = []
buckets = []





def print_results(buckets):
    print(termcolor.colored("Buckets without Encryption!", color="red",attrs=["bold"]))
    for bucket in buckets:
        print(f'- Bucket: {termcolor.colored(bucket, "blue", attrs=["bold"])}')


def get_public_buckets():
    """
    Gets s3 buckets that are public access.
    :param AWS_ROLE: this parameter, passe how account will be usade.
    :return: None.
    """
    
    # Connection with S3
    s3_resource = boto3.Session().resource("s3")
    s3_client = boto3.Session().client("s3")
    
    
    # Getting bucket list names
    buckets_list = s3_resource.buckets.all()
    
    
    # Getting all infotion security about the buckets
    for bucket in buckets_list:
        if bucket.name not in EXCEPTION_BUCKET_LIST:
            bucket_name = bucket.name
            encryption = get_buckets_without_encryption(s3_client, bucket_name)
            if encryption == False:
                buckets.append(bucket_name)
            
    return buckets
            
        
        
        
    
    
    



if __name__=="__main__":
    buckets = get_public_buckets()
    print_results(buckets)
    