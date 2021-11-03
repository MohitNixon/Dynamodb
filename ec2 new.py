import sys
import boto3


ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-091a9fc5b84d4b1d2'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-091a9fc5b84d4b1d2'])
print(response)