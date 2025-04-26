import boto3

rds_client = boto3.client('rds', region_name='ap-south-1')

db_instance_id = 'Database-1'

response = rds_client.delete_db_instance(
    DBInstanceIdentifier=db_instance_id,
    SkipFinalSnapshot=True,  
    DeleteAutomatedBackups=True
)

print(f"Deletion initiated for RDS instance: {db_instance_id}")
print("Status:", response['DBInstance']['DBInstanceStatus'])