import argparse
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="Run code with logging capabilities")
parser.add_argument('--file', default='input.txt', help='File name to open')
parser.add_argument('--log', default='INFO', help='Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)')
parser.add_argument('--lfn', default='build.log', help='*.log file name')
args = parser.parse_args()

log_level = getattr(logging, args.log.upper(), None)
if not isinstance(log_level, int):
  raise ValueError(f'Invalid log level: {args.log}')
logger.setLevel(log_level)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler to write logs to a file
file_handler = logging.FileHandler(args.lfn, 'w')
file_handler.setLevel(log_level)
file_handler.setFormatter(formatter)

# Create a stream handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
