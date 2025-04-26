import boto3

# Initialize session and S3 client
session = boto3.session.Session(profile_name="default", region_name="us-east-1")
s3 = session.client("s3")

# Upload file
local_file_path = "C:/Users/User/Desktop/matches.csv"
bucket_name = "paulrohit804bucket"
s3_key = "uploads/matches.csv"

try:
    s3.upload_file(local_file_path, bucket_name, s3_key)
    print(f" File uploaded to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(f" Upload failed: {e}")
