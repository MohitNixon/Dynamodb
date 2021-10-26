import boto3
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table("DemodataBase")
response = table.get_item(
    Key={
        'ID': '002',
        'phone':'6789876676',
    }
)
item = response['Item']
print(item)