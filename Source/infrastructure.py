import configparser
import os

config = configparser.ConfigParser()
config.read('config.cfg')

os.environ['AWS_ACCESS_KEY_ID'] = config['KEYS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['KEYS']['AWS_SECRET_ACCESS_KEY']

def create_iam_role():
    pass

def create_s3_bucket():
    pass
