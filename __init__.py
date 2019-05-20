"""AWS"""

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Amazon web service"
__version__ = "0.1"
__trigger__ = "aws "
__author__ = "Bharat kalluri"
__dependencies__ = []

AWS_SERVICES_LIST = [
    {
        "name": 'AWS EC2',
        "url": "https://console.aws.amazon.com/ec2"
    },
    {
        "name": 'AWS ECS',
        "url": "https://console.aws.amazon.com/ecs"
    },
    {
        "name": 'AWS RDS',
        "url": "https://console.aws.amazon.com/RDS"
    },
    {
        "name": 'AWS S3',
        "url": "https://s3.console.aws.amazon.com/s3"
    },
    {
        "name": 'AWS Elasticbeanstalk',
        "url": "https://console.aws.amazon.com/elasticbeanstalk"
    },
    {
        "name": 'AWS ElastiCache',
        "url": "https://console.aws.amazon.com/elasticache"
    },
    {
        "name": 'AWS CloudWatch',
        "url": "https://console.aws.amazon.com/cloudwatch"
    },
    {
        "name": 'AWS Cloudformation',
        "url": "https://console.aws.amazon.com/cloudformation"
    },
    {
        "name": 'AWS Route53',
        "url": "https://console.aws.amazon.com/route53"
    },
    {
        "name": 'AWS VPC',
        "url": "https://console.aws.amazon.com/vpc"
    },
    {
        "name": 'AWS IAM',
        "url": "https://console.aws.amazon.com/iam"
    },
    {
        "name": 'AWS ECR',
        "url": "https://console.aws.amazon.com/ecr"
    },
    {
        "name": 'AWS EKS',
        "url": "https://console.aws.amazon.com/eks"
    },
    {
        "name": 'AWS Lambda',
        "url": "https://console.aws.amazon.com/lambda"
    },
    {
        "name": 'AWS Dynamo DB',
        "url": "https://console.aws.amazon.com/dynamodb"
    },
    {
        "name": 'AWS Management Console',
        "url": "https://console.aws.amazon.com"
    },
    {
        "name": 'AWS Pricing calculator',
        "url": "https://calculator.s3.amazonaws.com/index.html"
    }
]


def handleQuery(query):
    if query.isTriggered and query.string.strip():
        if not query.isValid:
            return
        clean_query = query.string.replace(" ", "")
        filtered_list = AWS_SERVICES_LIST
        if len(clean_query) > 1:
            filtered_list = [el for el in filtered_list if clean_query in el['name'].lower()]
        if clean_query:
            return [Item(
                id=__prettyname__,
                text=el['name'],
                actions=[UrlAction(f"Open {el['name']}", el['url'])]
            ) for el in filtered_list]
