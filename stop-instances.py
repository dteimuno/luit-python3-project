import boto3

ec2 = boto3.client('ec2')
instanceids = ['i-06c5283867762f1e8','i-089507aec9d2f0216','i-0358cf3e42ddcedcb']

response = ec2.stop_instances(InstanceIds=instanceids)

