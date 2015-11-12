import boto3

def get_url_from_alias(alias=''):
    if alias == '':
        alias = '/'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('diegor_me')
    search = {'alias': alias}
    response = table.get_item(Key=search)
    item = response.get('Item')
    if item:
        return item.get('url')
