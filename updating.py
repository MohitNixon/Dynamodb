import boto3
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table("DemodataBase")

table.update_item(
    Key={
        'ID': '001',
        'phone': '9876543567'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)