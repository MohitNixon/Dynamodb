import  boto3
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table("DemodataBase")
table.put_item(
   Item={
        'ID': '008',
        'phone' :'5444521',
        'name': 'new',

    }
)