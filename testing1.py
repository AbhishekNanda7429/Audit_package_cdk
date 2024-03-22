from Package import audit
import logging

# Create a logger
logger = logging.getLogger(__name__)

clb_name = "E"
esp_name = "nos"
record_fetched = 100
success_record = 61
failure_record = 39
 

# Upload JSON data to S3 using the package function
success = audit.audit(clb_name, esp_name,record_fetched,success_record,failure_record)

if success:
    logger.info("JSON data uploaded to S3 successfully")
else:
    logger.error("Failed to upload JSON data to S3")
