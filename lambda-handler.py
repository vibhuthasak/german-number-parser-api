import json
import boto3
from pymongo import MongoClient
from bson.objectid import ObjectId

s3_client = boto3.client("s3")
client_docdb = MongoClient(
    "mongodb://master1:EnybGU522#xLZw@docdb-2022-12-05-07-41-33.cluster-cnpeiwumekol.ap-southeast-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false&tls=false",
    connect=False,
)


def lambda_handler(event, context):

    event_body = json.loads(event["Records"][0]["body"])
    task_id = event_body["taskId"]
    bucket_name = event_body["BucketName"]
    file_key = event_body["FileKey"]

    print(task_id, bucket_name, file_key)

    process_file = s3_client.get_object(Bucket=bucket_name, Key=file_key)[
        "Body"
    ].iter_lines()

    num_list = set()

    for line in process_file:
        if line == "":
            continue
        decoded_line = line.decode("utf-8")
        strippedLine = decoded_line.strip().replace(" ", "")
        if strippedLine.startswith("0049") and len(strippedLine) == 15:
            num_list.add(strippedLine)
        elif strippedLine.startswith("+49") and len(strippedLine) == 14:
            num_list.add(strippedLine)

    print(num_list)

    # Inserting results to the document
    result = client_docdb.externaldb.tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"results": num_list}, "$currentDate": {"lastModified": True}},
    )
    print(result)

    return {"statusCode": 200, "body": "OK"}
