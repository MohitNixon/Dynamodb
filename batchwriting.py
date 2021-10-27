import boto3
dynamodb= boto3.resource('dynamodb')
table=dynamodb.Table("DemodataBase")
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'ID': '200',
            'phone': '77878',
            'age': '45',

        }
    )
    batch.put_item(
        Item={
            'ID': '201',
            'phone': '44597754',
            'age': '45',

        }
    )
    batch.put_item(
        Item={
            'ID': '202',
            'phone': '5522134',
            'age':'45',

        }
    )
    batch.put_item(
        Item={
            'ID': '204',
            'phone': '55566311',
            'age': '53',


        }
    )