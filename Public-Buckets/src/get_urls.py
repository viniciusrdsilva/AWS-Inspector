import re
from typing import List
import warnings
import requests


def get_urls(bucket_name) -> List:
    """
    Scans standard bucket urls.
    Returns only publicly accessible urls.
    :param bucket_name: Name of the bucket.
    :return: List that contains publicly accessible urls.
    """
    domain = "s3.amazonaws.com"
    access_urls = []
    urls_to_scan = [
        "https://{}.{}".format(bucket_name, domain),
        "http://{}.{}".format(bucket_name, domain),
        "https://{}/{}".format(domain, bucket_name),
        "http://{}/{}".format(domain, bucket_name)
    ]
    warnings.filterwarnings("ignore")
    for url in urls_to_scan:
        try:
            content = requests.get(url).text
        except requests.exceptions.SSLError:
            continue
        if not re.search("Access Denied", content):
            access_urls.append(url)
    return access_urls