#Final Lambda function code which was used to trigger a function stop in conjunction with an HTTP API.

import boto3


ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    filters = [{
            'Name': 'tag:Environment',
            'Values': ['Dev']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

    
   #filter the instances

    instances = ec2.instances.filter(Filters=filters)


    #locate all running instances

    RunningInstances = [instance.id for instance in instances]
 

    if len(RunningInstances) > 0:
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        return {
            "statusCode": 200,
            "body": f'Stopped instances: {RunningInstances}'
        }
        
    else:
        return {
            "statusCode": 200,
            "body": 'There are no instances to shutdown'
        }
        
