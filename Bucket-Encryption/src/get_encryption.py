from typing import List



def get_buckets_without_encryption(s3_client, bucket_name) -> bool:
    """
    Verify if the bucket has encryption activated
    :param bucket_name: Name of the bucket.
    :return: Boolean if the buck has or not encryption activated
    """
    try: 
        encryption = s3_client.get_bucket_encryption(Bucket=bucket_name)
        return True
    except:
        return False
        