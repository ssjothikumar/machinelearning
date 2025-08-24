import logging
import os
from datetime import datetime

# Create timestamped log file name
LOG_FILE = f"log_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create only the logs directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Create full file path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

