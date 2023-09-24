import configparser
import os
import boto3
from botocore.exceptions import ClientError

config = configparser.ConfigParser()
config.read('Source\config.cfg')

os.environ['AWS_ACCESS_KEY_ID'] = config['KEYS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['KEYS']['AWS_SECRET_ACCESS_KEY']
region_name = config['REGION']['REGION_NAME']
bucket_name = config['S3']['RAW_DATA_BUCKET']

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


def create_s3_bucket():
    # create if not exists
    s3 = boto3.client('s3', region_name=region_name)

    # Check if the bucket exists
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"The bucket '{bucket_name}' already exists.")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            # The bucket does not exist, so create it
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region_name}
            )
            print(f"Created the bucket '{bucket_name}' in region '{region_name}'.")
        else:
            # Something else went wrong
            print(f"An error occurred: {e}")
    

def write_to_s3(file_name):
    s3 = boto3.client('s3', region_name=region_name)

    if os.path.isfile(file_name):
        # if file exists, write it to S3
        s3.upload_file(file_name, bucket_name, file_name)
    else:
        print(f"File not found!: {file_name}")
