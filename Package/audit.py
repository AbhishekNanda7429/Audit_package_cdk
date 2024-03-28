import json
import boto3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# #get the bucketname
bucket_name = 'onetrust-input'

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

        # Get the current date and time
        current_datetime = datetime.now()

        # Format the current date and time as a string
        formatted_datetime = current_datetime.strftime("%Y/%m/%d/%H/%M")

        # Create the filename using the formatted date and time
        filename = f"{clb_name}/{formatted_datetime}/{correlation_id}.json"

        # Convert JSON data to a JSON string
        json_string = json.dumps(json_data)
        
        # logger.info("filename:", filename)
        # logger.info("json_string:", json_data)
        # print(f"JSON String:", json_string)
        # print(f"Filename:", filename)
        # print(f"Bucket Name", bucket_name)
        
        # Create an S3 client
        s3_client = boto3.client('s3')
        
        # Upload JSON data to S3
        response = s3_client.put_object(
            Bucket= bucket_name,
            Key=filename,
            Body=json_string
        )
        logger.info("File uploaded successfully.")        
        return True
    
    except Exception as e:
        raise RuntimeError ("Error uploading JSON data to S3: ",e) 