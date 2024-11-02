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
        print(shuttingDown)

    else:
        print("There are no instances to shutdown")