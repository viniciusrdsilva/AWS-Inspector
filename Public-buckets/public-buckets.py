import boto3
import termcolor
from src.get_location import get_location
from src.get_permission import get_public_permission_informations
from src.get_urls import get_urls



# Creating variables
AWS_ROLE = 'staging'
buckets = {}




def print_results(buckets):
    for bucket in buckets:
        print("---------------------------------------")
        print(termcolor.colored("Public Bucket Found!", color="red",attrs=["bold"]))
        print(f'Bucket: {termcolor.colored(bucket, "blue", attrs=["bold"])}')
        print(f'Location: {buckets[bucket]["location"]}')
        for finding in buckets[bucket]["findings"]:
            print(f'Permission: {finding["permission"]} by {finding["access"]}')
        print("URLs:")
        for url in buckets[bucket]["urls"]:
            print(f'- {url}')


def get_public_buckets(AWS_ROLE):
    """
    Gets s3 buckets that are public access.
    :param AWS_ROLE: this parameter, passe how account will be usade.
    :return: None.
    """
    
    # Connection with S3
    session = boto3.Session(profile_name=AWS_ROLE)
    s3_resource = session.resource("s3")
    s3_client = session.client("s3")
    
    
    # Getting bucket list names
    buckets_list = s3_resource.buckets.all()
    
    
    # Getting all infotion security about the buckets
    for bucket in buckets_list:
        bucket_name = bucket.name
        bucket_acl = bucket.Acl()
        public_permission_list = get_public_permission_informations(bucket_acl)
        findings = []
        for finding in public_permission_list:
            if finding == []:
                break
            elif finding["public"] == False:
                break
            else:
                findings.append(finding)
        
        if len(findings) > 0:
            bucket_location = get_location(s3_client, bucket_name=bucket_name)
            bucket_urls = get_urls(bucket_name)
            buckets[bucket_name] = {"location": bucket_location, "findings" : findings, "urls": bucket_urls}
        
    return buckets
            
        
        
        
    
    
    



if __name__=="__main__":
    buckets = get_public_buckets(AWS_ROLE)
    print_results(buckets)
    