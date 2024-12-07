import os
import socket
import datetime
import time
import logging

# Configuration
FILE = os.path.join(os.getcwd(), "networkinfo.log")
MYHOST = "8.8.8.8"
MYPORT = 53
CHECK_INTERVAL = 5
RETRY_INTERVAL = 1

# Logging setup
logging.basicConfig(
    level=logging.INFO,  # Set the minimum logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# File handler
file_handler = logging.FileHandler(FILE)
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adding handlers to the logger
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def ping(host, port, timeout=3):
    """Check if the specified host and port are reachable."""
    try:
        socket.setdefaulttimeout(timeout)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
        return True
    except socket.error:
        return False

def calculate_time(start, stop):
    """Calculate the time difference in seconds."""
    return (stop - start).total_seconds()

def monitor_connection():
    """Monitor the network connection and log events."""
    logger.info("Monitoring started.")
    while True:
        if ping(MYHOST, MYPORT):
            time.sleep(CHECK_INTERVAL)
            print("ping OK")
        else:
            down_time = datetime.datetime.now()
            logger.warning(f"Connection lost at {down_time}.")
            while not ping(MYHOST, MYPORT):
                time.sleep(RETRY_INTERVAL)
            up_time = datetime.datetime.now()
            duration = calculate_time(down_time, up_time)
            logger.info(f"Connection restored at {up_time}.")
            logger.info(f"Connection was unavailable for {duration:.2f} seconds.")

if __name__ == "__main__":
    try:
        monitor_connection()
    except KeyboardInterrupt:
        logger.info("Monitoring stopped by user.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
