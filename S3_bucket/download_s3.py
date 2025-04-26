import boto3

# Initialize session and S3 client
session = boto3.session.Session(profile_name="default", region_name="us-east-1")
s3 = session.client("s3")

# Download file
bucket_name = "paulrohit804bucket"
s3_key = "uploads/matches.csv"
local_download_path = "C:/Users/User/Desktop/downloaded_matches.csv"

try:
    s3.downlotad_file(bucket_name, s3_key, local_download_path)
    print(f" File downloaded to: {local_download_path}")
except Exception as e:
    print(f" Download failed: {e}")
