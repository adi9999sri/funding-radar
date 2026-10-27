import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    obj = s3.get_object(Bucket="YOUR-BUCKET-NAME", Key="funding.json")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Cache-Control": "max-age=300",
        },
        "body": obj["Body"].read().decode("utf-8"),
    }
