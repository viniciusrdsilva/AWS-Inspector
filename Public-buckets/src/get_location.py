


def get_location(s3_client, bucket_name) -> str:
    """
    Returns the bucket location.
    :param bucket_name: Name of the bucket.
    :param s3_client: s3_client instance.
    :return: String with bucket's region.
    """
    location = s3_client.get_bucket_location(
            Bucket=bucket_name)["LocationConstraint"]
    if location is None:
        location = "us-east-1"
    return location