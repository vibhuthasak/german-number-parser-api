import boto3, logging, json

logger = logging.getLogger(__name__)

sqs_client = boto3.client("sqs")
s3_client = boto3.client("s3")

# Publish messege to SQS
def publishToProcessQueue(message):
    try:
        response = sqs_client.send_message(
            QueueUrl="https://sqs.ap-southeast-1.amazonaws.com/307676294310/numbers-to-process",
            MessageBody=json.dumps(message),
        )
    except Exception as error:
        logger.exception("Save failed")
        return {"error": True, "description": str(error)}
    else:
        return {"error": False, "description": response}


def saveFileOnS3(file, key):
    try:
        response = s3_client.upload_file(
            Filename=file,
            Bucket="numberfiles-german-numbers",
            Key=key,
        )
    except Exception as error:
        logger.exception("Save failed")
        return {"error": True, "description": str(error)}
    else:
        return {"error": False, "description": response}


def fileValidator(file):
    # Should be a text
    if file.content_type != "text/plain":
        return False
    else:
        return True
