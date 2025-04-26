import boto3

s3_bucket = boto3.client('s3')

bucket_name = 'moibucket48'
region = 'ap-south-1' 

s3_bucket.create_bucket(
    Bucket = bucket_name ,
    CreateBucketConfiguration = {'LocationConstraint' : region}
)

print(f"Bucket : {bucket_name} Successfully Created!!...")