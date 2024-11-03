## API Gateway, Boto3 , Lambda, and EventBridge to Automate Stopping EC2 Instances At Pre-determined Times

![Dennis Tei-Muno](https://github.com/user-attachments/assets/e061eff4-5a8b-49bb-a184-19f010c2d75c)

# Project Outline:
This project has three parts from simple to complex:
- Part 1: Create A Python Script with Boto3 and Insert Into Lambda That Stops EC2 Instances At A Certain Time
- Part 2: Advanced: Use AWS EventBridge and AWS Lambda To Stop Specific Instances By Their Tags
- Part 3: Use AWS API Gateway to Create An HTTP API That Triggers My Lambda Function Based On Query Parameters

The GitHub Repository for this project can be found here(https://github.com/dteimuno/luit-python3-project)

# Introduction:
This project demonstrates the power of automation to stop EC2 instances using a Lambda function with Boto3 ec2 scripts modified to first stop instances at a given time, but also instances with a certain tag. Also performed was the merging of the Lambda function with AWS EventBridge to trigger my stop EC2 instances Lambda function at a certain time every day.
Also done was using an API to trigger the stopping of EC2 instances by creating via AWS API Gateway, an HTTP API that triggered my function to delete instances with a key-value tag combination of Environment: Dev.
This project showcases using AWS Lambda, EventBridge, and APIGateway APIs to automate tasks in AWS, which has uses in efficiency, cost-cutting, and automation to scale workloads efficiently and automatically without manually performing each task.

# Challenges I Faced:
- Failed Boto3 results Iteration
- AWS Lambda Return function ;for the API Gateway, you need a value for 'body' in the return function, or you'll get an error
- Generating Boto3 Script To Delete Instances Only With certain tag

# Technology/Tools Used:
- Visual Studio Code
- AWS EC2
- Boto3 Python Library
- AWS EventBridge
- AWS API Gateway
- AWS Lambda

# Implementation Steps

- To start this project, we will create a new Github repository for our code that will be used for this project. The repository was locked down
![image](https://github.com/user-attachments/assets/870a2b4b-9e7e-47c9-ad65-f23081f23471)

- I then created a new side branch where my initial changes would go to for approval before committing changes to the main branch:
![image](https://github.com/user-attachments/assets/28475ef2-d604-4571-901d-12ad86949c46)
- I will then clone my repository to my PC so I can work via Visual Studio Code(must have Github desktop installed):Click on "Code">"Open with GitHub Desktop"
![image](https://github.com/user-attachments/assets/aa7c5b41-e103-4963-84e9-a380941f6c44)
- We then clone the repository to my PC by clicking "Clone":
![image](https://github.com/user-attachments/assets/bbad1c53-dc83-4e41-9d29-0541a05d994e)
- I then open my repository in Visual Studio Code so my work can begin by clicking "Open in Visual Studio Code":
![image](https://github.com/user-attachments/assets/8ef3ea78-4bc8-458c-b505-1d80cfda7ee3)
- I create a file called "luit-project3.py" Where I will be testing out my code.
- For our project, we will be testing using boto3 to stop 3 ec2 instances, so I first need to create 3 ec2 instances. I will be creating 3 Ubuntu instances via VSC CLI with the command:
```
aws configure
#Type in your keys. AWS will require 2 keys

aws ec2 run-instances --image-id ami-0866a3c8686eaeeba \
--instance-type t2.micro \
--key-name keypairforluitccp3 \
--security-group-ids "sg-00d40412bcd8cbb19" \
--count 3
--output json
```
- We can confirm that our 3 ec2 instances are up and running:
![image](https://github.com/user-attachments/assets/4ea4cec1-1ee0-4c06-99cc-cb2ad666ee6f)

## Creating Python Script That Stops Our EC2 Instances
- I will be referencing AWS Boto3(the Python SDK for AWS manipulation) and modifying it to create the following script that will stop my instances. I will then save my script and input it into Visual Studio Code:
```
import boto3

ec2 = boto3.client('ec2')
response = client.stop_instances(
    InstanceIds=[
        'i-06c5283867762f1e8',
        'i-089507aec9d2f0216',
        'i-0358cf3e42ddcedcb'
    ],
    Hibernate=False,
    DryRun=False,
    Force=False
)
```

- I will then in the AWS console navigate to the Lambda service and click "Create Function":
![image](https://github.com/user-attachments/assets/b73c6ec8-db37-4b28-9800-a8288a5561e1)
- I will use the following configurations:
![image](https://github.com/user-attachments/assets/c99b11e7-d853-42ea-9b03-1759c612bfaf)
- Under the Permissions section, since we will be using Lambda to stop Ec2 instances we will need to give our Lambda function the ability to stop ec2 instances. Hence we will need to create an IAM Role. A basic Lambda function will not work for us.
- We will navigate to the IAM console in a new tab and use the following configurations:
![image](https://github.com/user-attachments/assets/80af34fe-533b-4657-ad01-f86667184b36)
- I then chose the following managed policies on page 1 which showed up on my review page:
![image](https://github.com/user-attachments/assets/85329685-1497-4836-90d8-bfd804bcccad)
- The first policy "AWSLambdaBasicExecutionRole" allows for basic Lambda functions to be done. The "AmazonEC2RolePolicyForLaunchWizard" policy allows for my Lambda function to be able to do many things, including delete an instance.
![image](https://github.com/user-attachments/assets/f582cc20-6539-41c0-8a40-290e3fb1ebbd)
- I gave my IAM Role a name and then clicked on "Create Role" To create my IAM Role that I would assign to my Lambda function.
- I navigated back to my Lambda function I was creating, and under "Change Default Execution Role" I selected "Use an Existing Role". I then selected my previous role I created:
![image](https://github.com/user-attachments/assets/7666a2a4-82f7-46b3-bb95-0f91007d308e)
- I then clicked on "Create Function" to create my Lambda function:
![image](https://github.com/user-attachments/assets/e10c735d-2a2f-48a4-b407-15f9d68939b7)
![image](https://github.com/user-attachments/assets/def61c4e-edee-46f3-89eb-a7f0d61d804b)

# Editing Our Lambda Function Code
- On our function page we we navigate to the "Code" subsection and then input our python script to run:
```python
import boto3

ec2 = boto3.client('ec2')
instanceids = ['i-06c5283867762f1e8','i-089507aec9d2f0216','i-0358cf3e42ddcedcb']

def lambda_handler(event, context):
    ec2.stop_instances(
    InstanceIds=instanceids,
    Hibernate=False,
    DryRun=False,
    Force=False
)
    print('The ff instances were stopped:', instanceids)
```
![image](https://github.com/user-attachments/assets/62222e6a-3954-42c2-bf84-434105093c74)
- We will then click deploy right above our function input to deploy our changes.
- Once our changes have been deployed, we will move to the "configuration" subsection and then under "General configuration" we will click "Edit".
- We will then change our "Timeout" to 10 seconds and then click "Save":
![image](https://github.com/user-attachments/assets/aa9478d8-adda-4219-877a-fe44298e7aa3)

# Testing Our Lambda Function
- In our code subsection, we will click on the "Test" dropdown button and then click on "Configure Test event" to test the function:
![image](https://github.com/user-attachments/assets/1a06b923-e988-4c0c-919d-7cfc128565ef)

# Reworking the Lambda IAM Role Permission Policies
- My test event showed a failure which appears to be an IAM policy failure. I will navigate to IAM>Policies>Create Policy and try out a new policy from AWS docs:
```json
{  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",
        "ec2:Stop*"
      ],
      "Resource": "*"
    }
  ]
}
```
![image](https://github.com/user-attachments/assets/ff8c0670-497b-4d8d-85b8-8be85fe4497c)
- I then created the policy:
![image](https://github.com/user-attachments/assets/af64ee5d-d085-43a6-a4a8-81c9c98d93cf)
- I then navigated to IAM>Roles and selected my Role created for my Lambda function. I then deleted the policies that were attached:
![image](https://github.com/user-attachments/assets/60c81b5b-7d1f-4326-87c0-7cf4232d4744)
- I then under permissions policies clicked on "Add permissions" and added the new policy I just created. I then clicked on "Add permissions":
![image](https://github.com/user-attachments/assets/53505f39-ab3a-4421-b38b-fe10315e992d)

# Lambda Function Try #2
- I clicked on "Test" again, and boom!- It worked!:
![image](https://github.com/user-attachments/assets/805bd75e-aada-4b80-bc9d-6af521088b34)
When we navigate to our EC2 instance we see that our Lambda function did turn off our instances:
![image](https://github.com/user-attachments/assets/75a799cf-b3d9-4d14-bc20-dd99c1c66a7a)

# Create EventBridge Rules That Allow For Stop Ec2 Lambda Function To Work At A Specific Time
- I will navigate to the EventBridge service.
- I will then click on "EventBridge Rule" and then "Create Rule":
![image](https://github.com/user-attachments/assets/08ace955-48ce-4db9-b260-6291cc496cd8)
- For page 1, I will use the following settings:
![image](https://github.com/user-attachments/assets/764915b1-3967-450e-bbf0-8383eaad4230)
![image](https://github.com/user-attachments/assets/34d38f97-7475-4b1e-a508-de64f5c9b107)
![image](https://github.com/user-attachments/assets/6d14870e-2c35-46fa-bd11-8199ede1a7aa)
- I then on the next page select my Target as AWS Lambda and select my Lambda function:
![image](https://github.com/user-attachments/assets/198d4c8a-7899-4c99-9279-b7d43d1fdb46)
![image](https://github.com/user-attachments/assets/2aaf1b52-8175-45dc-90a9-d86c80ef362c)
- We leave the payload empty and then click "Skip to Review and create schedule":
![image](https://github.com/user-attachments/assets/aa721e15-fb2a-472a-b7c7-69087d6d6d3e)
- I then waited to see if my schedule worked. It is currently 2:36AM in Denton TX, UT -05:00 on November 2, 2024.
![image](https://github.com/user-attachments/assets/882c4de4-02cb-4767-8c93-3e053730ef11)
- I will wait till it is 2:40 and then see if it will work then.
- It is currently 2:37Am(3 minutes to go) and my instances are still running.
- At 2:40AM AWS Event Bridge activates my Lambda function to stop my instances:
![image](https://github.com/user-attachments/assets/ab42ddcd-9df2-45a5-a820-da523cbe64b9)
- I will be modifying the time this function should run every day to 7PM as this is the requirement for this project.
- To do so, I will navigate to AWS EventBridge>Schedules>MySchedule>Edit> and change my cron expression to the following:
![image](https://github.com/user-attachments/assets/b2e8049e-53f1-4edc-8826-f09988a1fe69)
- This will allow my function to run everyday at 7PM. I will then save my schedule.

## Advanced: Use AWS EventBridge and AWS Lambda To Stop Specifc Instances By Their Tags
- I will create two new instances with the tag "Environment(key): Dev(value)"
![image](https://github.com/user-attachments/assets/324d72af-573e-438f-ab98-0fb0b233f010)
![image](https://github.com/user-attachments/assets/fab905f9-8660-4f2e-9cdf-1076d43ac589)
- I renamed my instances so I could easily sort them out after processing my results.
- I have also ensured my instances are all turned back on(5 of them; 2 tagged, 3 untagged)
- I will then navigate to my IAM Role for my Lamda Function and then add the "EC2FullAccess" policy to my IAM Role
![image](https://github.com/user-attachments/assets/4936d743-a320-450f-986c-f8394aa02d47)
- Instead of using the ec2 boto3 ec2.stop_instances API call I will be using the ec2.describes instances API call for the first part.
- My boto3 script will look like this and I will try running it:
```python
import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': [
                'Dev',
            ]
        },
    ],
)
```
- Did not work!
![image](https://github.com/user-attachments/assets/1ec2dfb6-1390-4e4b-ae28-790a5d294e43)
- I have confirmed that my instances run:
![image](https://github.com/user-attachments/assets/f61c1505-0649-4765-9a5c-bea4c0a25f36)
- Let me deploy and run my Lambda function and see if it will work:
![image](https://github.com/user-attachments/assets/32a47f45-0161-42da-a661-edf25de7ed90)
- I will move to IAM Policies and create one with the following information:
```json
{
"Version": "2012-10-17",
"Statement": [
    {
        "Sid": "VisualEditor0",
        "Effect": "Allow",
        "Action": "ec2:DescribeInstances",
        "Resource": "*"
    }
]
}
```
- For my tags, I will add the tag with Key: Environment, and Value:Dev. This should help search for my instances that are tagged my easily:
![image](https://github.com/user-attachments/assets/42d25308-ca72-4239-9466-f24aeea28699)
- I will then attach this policy to my Lambda Function IAM Role.
- I will try running my Lambda function again with new code:
```python
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
```
- The result from Lambda:
![image](https://github.com/user-attachments/assets/b113fe35-0d15-44f3-a9d3-a5aa74b93242)
- From Ec2, we see that our code worked. The instances with the tag- Key= Environment: Dev were stopped. The other EC2 instances were still running.
![image](https://github.com/user-attachments/assets/690dabcd-cff9-43b5-8014-5b990c876058)

## Part 3: Use AWS API Gateway to Create An HTTP API That Triggers My Lambda Function Based On Query Parameters

# Getting My EC2 Instances Running Again
- I will start all my EC2 instances again:
![image](https://github.com/user-attachments/assets/9d0de508-5bc1-4044-89ee-6238849f2a2e)

# Setting Up A Trigger For My Lambda Function
- I first have to make sure my instances are all turned on again. All five of them.
- I will navigate to my Lambda function and on my function page I will click "Add Trigger"
![image](https://github.com/user-attachments/assets/2d3049f7-28a7-434f-8004-1e1d57d0d1d1)
- I will use the following settings:
![image](https://github.com/user-attachments/assets/03a386a8-3b0b-499c-80ac-c420cabe1f9d)
![image](https://github.com/user-attachments/assets/0376bde2-b85a-4a51-b310-42afb749842f)
- I then click "Add" to add my API as a trigger for my Lambda function.
- I will then click on my API Gateway Trigger:
![image](https://github.com/user-attachments/assets/9345bb8b-febf-4ab3-90b5-2442bb320f53)
- We will navigate to configuration> "Triggers" and click on the API endpoint link:
![image](https://github.com/user-attachments/assets/f5e741ec-cc9e-4cb1-bdcb-3bdd0f41e10e)
- I get an error message:
![image](https://github.com/user-attachments/assets/f2e95b46-517d-413d-8e59-e294fa0e3e6f)
- However, I after navigating to my running Ec2 instances I see that my two tagged instances are no longer running:
![image](https://github.com/user-attachments/assets/9fc2a8a6-f540-469c-88d4-1f973bb49edb)
- This means my API invocation of my Lambda function worked, however we have a few issues going on.

# Troubleshooting The {"message":"Internal Server Error"} Issue
![image](https://github.com/user-attachments/assets/ec8eb898-a5a2-486b-bbee-34cf69ab9548)
- It appears the reason for this error shown(even though my Lambda function worked fantastically) is that my function code did not have a body, statusCode, and headers variable value. I will have to add that to my Lambda function and deploy it before calling my API.
- I will ensure that all my instances are up again:
![image](https://github.com/user-attachments/assets/f285f87c-dad3-40a2-9973-f645564e5713)
I will then modify my code after doing some research to work for particular situation:
```python
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
```
- After testing my event in Lambda, I got the following feedback from Lambda:
![image](https://github.com/user-attachments/assets/c15ec265-2e68-48fe-90d4-a3100e45afdc)
- My function invocation also turned my tagged instances off as confirmation:
![image](https://github.com/user-attachments/assets/6db202d3-1492-4615-bd71-d8084dc5bd9c)

# Finally Trying Out My API Invocation To See If It Will Work Without The Error Message
- I will get all my stopped instances back on again:
![image](https://github.com/user-attachments/assets/2fc51eee-678a-48ac-b11b-9a2fe273ca01)
- Under my Lambda function landing page, I will click on the "Configuration" subsection and click on my API endpoint link:
![image](https://github.com/user-attachments/assets/f770d226-8b53-4ed4-b1f5-d46c4a7e2ad0)
- We will click on the link to invoke the function:
![image](https://github.com/user-attachments/assets/8912bcd1-67ca-4900-aa08-4c4b5c8e0780)
- And voila! The HTTP API triggered our function with output shown on the page:
![image](https://github.com/user-attachments/assets/6e84b34e-4734-48c2-95ec-b67147c69195)
- From my EC2 page, you can see my two tagged instances were stopped because my API invoked the function containing instructions to stop instances based on the Tag-key-value Environment = Dev:
![image](https://github.com/user-attachments/assets/57039405-a1ce-42e9-9885-2cb6d56a7b01)

# CleanUp- Don't Rack Up Costs or Leave Resources Running!
- Delete your EC2 instances
- Delete your EventBridge Schedule

# Sources
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#ec2
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/stop_instances.html
https://repost.aws/knowledge-center/start-stop-lambda-eventbridge
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
https://www.youtube.com/watch?v=nYMLbpSG7j4&t=452s
