import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from google_images_search import GoogleImagesSearch

table_name = 'scrape-google-images-url'

client = boto3.client('dynamodb', region_name='eu-west-3',
                      aws_access_key_id='AKIAJUT7RTNWU5DRJXVQ',
                      aws_secret_access_key='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')

tmp = 'https://sun1-24.userapi.com/impg/c853628/v853628852/1f9990/STE1qgZYLF8.jpg?size=1200x1600&quality=96&proxy=1&sign=27ec6271c29d8d5a319e4ac924ac1828'
gis = GoogleImagesSearch('AIzaSyCJCs7A4UrfS5Bc7NwvI91JYT71-JxZKPc', '017576662512468239146')
f = open('count.txt', 'r')

for category in f.readlines():
    _search_params = {
        'q': category,
        'num': 200,
        'safe': 'off'
    }
    gis.search(search_params=_search_params, path_to_dir='/download/', width=224, height=224)

f.close()

# try:
#     response = client.put_item(
#         TableName=table_name,
#         Item={
#             'url': {'S': f'{tmp}'},
#             'category': {'S': 'пиздец'}
#         }
#     )
# except ClientError as err:
#     print(err)
