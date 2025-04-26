import boto3

# Start session in the correct region
aws_management_console = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2_console = aws_management_console.client(service_name="ec2")

 # Replace with your instance ID                 #to stop instance
# instance_id = "i-042ac008d11211141"
# Launch EC2 instance
try:
    result = ec2_console.run_instances(
        ImageId="ami-0e449927258d45bc4",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1,
        KeyName="rohit_bl_key_pair",
        SecurityGroupIds=["sg-0084140b3ca597cdc"],
        SubnetId="subnet-0990b3130c65d46eb",
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'AWSBoto3_instance'}]
            }
        ]
    )
    instance_id = result['Instances'][0]['InstanceId']
# response = ec2_client.stop_instances(InstanceIds=[instance_id])       #to stop instance
    print(f" Successfully launched instance: {instance_id}")
except Exception as e:
    print(f" Error launching instance: {e}")
# ------------------------------------------------------------to stop instance ------------------------------------------------------------
# import boto3

# # Create session and EC2 client
# aws_session = boto3.session.Session(profile_name="default", region_name="us-east-1")
# ec2_client = aws_session.client(service_name="ec2")

# # Replace with your instance ID
# instance_id = "i-042ac008d11211141"

# # Stop the instance
# try:
#     response = ec2_client.stop_instances(InstanceIds=[instance_id])
#     print(f" Stopping instance: {instance_id}")
# except Exception as e:
#     print(f" Error stopping instance: {e}")