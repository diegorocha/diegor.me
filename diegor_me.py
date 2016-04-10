import boto3
from decouple import config

_REGION_NAME = config('region')
_ACCESS_KEY_ID = config('aws_access_key_id')
_SECRET_ACCESS_KEY = config('aws_secret_access_key')

def get_url_from_alias(alias=''):
    if alias == '':
        alias = '/'
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id=_ACCESS_KEY_ID,
                              aws_secret_access_key=_SECRET_ACCESS_KEY,
                              region_name=_REGION_NAME)
    table = dynamodb.Table('diegor_me')
    search = {'alias': alias}
    response = table.get_item(Key=search)
    item = response.get('Item')
    if item:
        return item.get('url')

def save(item):
  if isinstance(item, dict) and item.get('alias'):
      dynamodb = boto3.resource('dynamodb',
                                aws_access_key_id=_ACCESS_KEY_ID,
                                aws_secret_access_key=_SECRET_ACCESS_KEY,
                                region_name=_REGION_NAME)
      table = dynamodb.Table('diegor_me')
      table.put_item(Item=item)
      return True
