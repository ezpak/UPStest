import configparser
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Read the configuration file
config.read(os.path.join(current_dir, 'config.ini'))

# UPS API Configuration
UPS_API_BASE_URL = config.get('UPS_API', 'BASE_URL')
UPS_CLIENT_ID = config.get('UPS_API', 'CLIENT_ID')
UPS_CLIENT_SECRET = config.get('UPS_API', 'CLIENT_SECRET')

# Logging Configuration
LOG_FILE = config.get('LOGGING', 'LOG_FILE')
LOG_LEVEL = config.get('LOGGING', 'LOG_LEVEL')
