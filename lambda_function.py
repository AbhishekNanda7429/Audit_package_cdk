import boto3
import json
import uuid
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

from Package import audit

tracer = Tracer()
logger = Logger(
    log_uncought_exception=True,
    serialize_stacktrace=False,
    POWERTOOLS_LOG_DUPLICATION_DISABLE=True,
    POWERTOOLS_LOGGER_LOG_EVENT=True
)

queue_url = 'https://sqs.ap-south-1.amazonaws.com/891377261145/BufferQueue'

correlation_id = str(uuid.uuid4())
logger.append_keys(correlation_id=correlation_id)

clb_name = "E"
esp_name = "nos"
record_fetched = 100
success_record = 61
failure_record = 39
correlation_id = correlation_id

@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event,context):
    
    # Upload JSON data to S3 using the package function
    success = audit.audit(clb_name, esp_name,record_fetched,success_record,failure_record,correlation_id)

    
    sqs = boto3.client('sqs')
    
    json_data = event

    message_body = {
        'correlation_id': correlation_id,
        'data' : json_data
    }

    response = sqs.send_message(
     QueueUrl = queue_url,
     MessageBody = json.dumps(message_body)
    )
    logger.info("send the data to SQS!")

    return{
        'statusCode': 200,
        'body': json.dumps('JSON data send to SQS successfully')
    }