import sys
import boto3
from botocore.exceptions import ClientError

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')


if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=['i-091a9fc5b84d4b1d2'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=['i-091a9fc5b84d4b1d2'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=['i-091a9fc5b84d4b1d2'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=['i-091a9fc5b84d4b1d2'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)