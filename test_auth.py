from ups_api import UPSApi
from logger import setup_logger

def test_authentication():
    logger = setup_logger()
    ups_api = UPSApi(logger)

    try:
        ups_api.authenticate()
        print("Authentication successful! Access token obtained.")
    except Exception as e:
        print(f"Authentication failed: {str(e)}")

if __name__ == "__main__":
    test_authentication()
