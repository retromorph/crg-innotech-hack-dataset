import json
subprocess.call('pip install urlparse boto3 requests pillow  -t /tmp/ --no-cache-dir'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.path.insert(1, '/tmp/')
import urlparse
import boto3
import os
import requests
from io import BytesIO
from PIL import Image
import sys
import uuid
from urllib.parse import unquote_plus

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            url, category = record['dynamodb']['NewImage']['url']['S'], record['dynamodb']['NewImage']['category']['S']
            client = boto3.client('s3', region_name='eu-west-3')
            path = urlparse.urlparse(url).path
            name = uuid.uuid4() + '.' + os.path.splitext(path)[1]
            client.upload_file(category + '/' + url, 'crg-innotech-scrape-images-bucket', name)