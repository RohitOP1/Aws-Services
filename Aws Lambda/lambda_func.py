import json
import base64
import os
import boto3

s3_client = boto3.client('s3')  # Changed from resource to client, which is more standard for file uploads
s3_bucket_name = "moibucket48"

def lambda_handler(event, context):
    print(f"Event collected: {event}")
    for record in event['Records']:
        try:
            # Decode the base64-encoded Kinesis data
            sample_string_bytes = base64.b64decode(record['kinesis']['data'])
            sample_string = sample_string_bytes.decode("utf-8")  # It's better to use utf-8 encoding
            print(f"Decoded string: {sample_string}")

            # Create a dynamic file name based on the Kinesis record sequence number
            s3_file_name = f"{record['kinesis']['sequenceNumber']}.json"
            print(f"S3 bucket file name: {s3_file_name}")

            # Store the file temporarily in the Lambda /tmp directory
            local_file_path = f"/tmp/{s3_file_name}"
            print(f"Local file path: {local_file_path}")

            # Write the decoded data into the file
            with open(local_file_path, 'w') as fp:
                json.dump(json.loads(sample_string), fp)
            print("Event data written to local file")

            # Upload the file to S3
            s3_client.upload_file(local_file_path, s3_bucket_name, s3_file_name)
            print(f"File uploaded successfully to {s3_bucket_name}/{s3_file_name}")

            # Clean up the local file after uploading
            os.remove(local_file_path)
            print(f"Local file deleted after upload to S3")

        except Exception as e:
            print(f"Error processing record: {str(e)}")
            continue  # Skip to the next record if an error occurs
