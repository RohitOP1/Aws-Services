import boto3

rds = boto3.client('rds')

response = rds.create_db_instance(
    DBInstanceIdentifier='Database-1',
    DBInstanceClass='db.t3.micro',
    Engine='postgres',
    MasterUsername='postgres',
    MasterUserPassword='adityakumar',
    AllocatedStorage=20,
    BackupRetentionPeriod=7,
    VpcSecurityGroupIds=['sg-xxxxxxxx'],
    AvailabilityZone='ap-south-1a',
    PubliclyAccessible=True
)

print(response)