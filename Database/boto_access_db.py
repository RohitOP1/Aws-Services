import boto3
from botocore.exceptions import ClientError

region = 'ap-south-1'

db_instance_id = 'database-1'

rds_client = boto3.client('rds', region_name=region)

try:
    response = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance_id)
    db = response['DBInstances'][0]

    print("Connected to RDS! Here are the details:")
    print(f"Endpoint            : {db['Endpoint']['Address']}")
    print(f"Port                : {db['Endpoint']['Port']}")
    print(f"Engine              : {db['Engine']}")
    print(f"Engine Version      : {db['EngineVersion']}")
    print(f"Instance Class      : {db['DBInstanceClass']}")
    print(f"DB Name             : {db.get('DBName', 'Not set')}")
    print(f"Master Username     : {db['MasterUsername']}")
    print(f"VPC ID              : {db['DBSubnetGroup']['VpcId']}")
    print(f"Publicly Accessible : {'Yes' if db['PubliclyAccessible'] else 'No'}")
    print(f"Storage             : {db['AllocatedStorage']} GB")
    print(f"Status              : {db['DBInstanceStatus']}")
    print(f"Availability Zone   : {db['AvailabilityZone']}")

except ClientError as e:
    print(f"Boto3 Error: {e.response['Error']['Message']}")
except Exception as e:
    print(f"Unexpected Error: {str(e)}")
