import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")
# List Instances
result=ec2_console.describe_instances()
# print(result)
for each_instance in result:
    for each_instance_detail in result:
        print(each_instance)
        # print(each_instance_detail["InstanceId"], each_instance_detail["InstanceType"], each_instance_detail["State"]["Name"])

