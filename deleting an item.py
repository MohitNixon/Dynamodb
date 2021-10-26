import boto3
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table("DemodataBase")
table.delete_item(
    Key={
         'ID': '003',
        'phone':'9113266608',
    }
)