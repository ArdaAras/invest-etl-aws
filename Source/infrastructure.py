import configparser
import os
import boto3

config = configparser.ConfigParser()
config.read('Source\config.cfg')

os.environ['AWS_ACCESS_KEY_ID'] = config['KEYS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['KEYS']['AWS_SECRET_ACCESS_KEY']
region_name = config['REGION']['REGION_NAME']

def create_cloudwatch_rule():
    # Initialize the CloudWatch client
    cloudwatch = boto3.client('events',region_name=region_name)

    # Define the rule name and schedule expression
    rule_name = 'DailyAt10PM'
    schedule_expression = 'cron(0 22 * * ? *)' # 10 PM which is after NASDAQ market closes for the day

    # Create the CloudWatch Events rule
    response = cloudwatch.put_rule(
        Name=rule_name,
        ScheduleExpression=schedule_expression,
        State='ENABLED'  # Set to 'ENABLED' to enable the rule immediately
    )

def create_iam_role():
    pass

def create_s3_bucket():
    pass
