import json
import boto3
import uuid
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# #get the bucketname
bucket_name = os.getenv('bucket')

def audit(clb_name,esp_name,record_fetched,success_record,failed_record,correlation_id):
    json_data= {
        "club_name": clb_name,
        "timestamp" : str(datetime.now()),
        "esp_name": esp_name,
        "number-of-records-fetched": record_fetched,
        "success-records": success_record,
        "failed-records": failed_record,
        "correlation_id": correlation_id
    }

    try:
        # Generate a UUID
        # unique_id = uuid.uuid4()

        # Convert UUID to string
        # unique_id_str = str(unique_id)

        # Get the current date and time
        current_datetime = datetime.now()

        # Format the current date and time as a string
        formatted_datetime = current_datetime.strftime("%Y/%m/%d/%H/%M")

        # Create the filename using the formatted date and time
        filename = f"{clb_name}/{formatted_datetime}/{correlation_id}.json"

        # Convert JSON data to a JSON string
        json_string = json.dumps(json_data)

        # Create an S3 client
        s3_client = boto3.client('s3')

        # Upload JSON data to S3
        response = s3_client.put_object(
            Bucket= bucket_name,
            Key=filename,
            Body=json_string
        )
        logger.info("File uploaded successfully.")
        # print(f"JSON data successfully uploaded to S3")
        return True
    except Exception as e:
        raise RuntimeError ("Error uploading JSON data to S3: ",e) 

