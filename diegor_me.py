import boto3
from decouple import config


def get_url_from_alias(alias=''):
    if alias == '':
        alias = '/'

    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id=config('aws_access_key_id'),
                              aws_secret_access_key=config('aws_secret_access_key'),
                              region_name=config('region'))
    table = dynamodb.Table('diegor_me')
    search = {'alias': alias}
    response = table.get_item(Key=search)
    item = response.get('Item')
    if item:
        return item.get('url')
