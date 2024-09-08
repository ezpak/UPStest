import requests
import base64
from config import UPS_API_BASE_URL, UPS_CLIENT_ID, UPS_CLIENT_SECRET

class UPSApi:
    def __init__(self, logger):
        self.logger = logger
        self.base_url = UPS_API_BASE_URL
        self.client_id = UPS_CLIENT_ID
        self.client_secret = UPS_CLIENT_SECRET
        self.access_token = None

    def authenticate(self):
        """Authenticate with UPS API and obtain access token."""
        auth_url = f"{self.base_url}/security/v1/oauth/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }
        
        try:
            response = requests.post(auth_url, headers=headers, data=data, auth=(self.client_id, self.client_secret))
            response.raise_for_status()
            self.access_token = response.json()["access_token"]
            self.logger.info("Successfully authenticated with UPS API")
        except requests.RequestException as e:
            self.logger.error(f"Failed to authenticate with UPS API: {str(e)}")
            raise

    def get_proof_of_delivery(self, tracking_number):
        """Retrieve Proof of Delivery data for a given tracking number."""
        if not self.access_token:
            self.authenticate()

        pod_url = f"{self.base_url}/track/v1/details/{tracking_number}"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(pod_url, headers=headers)
            response.raise_for_status()
            pod_data = response.json()
            self.logger.info(f"Successfully retrieved POD data for tracking number: {tracking_number}")
            return pod_data
        except requests.RequestException as e:
            self.logger.error(f"Failed to retrieve POD data: {str(e)}")
            raise

    def decode_pod_content(self, encoded_content):
        """Decode Base64-encoded POD content."""
        try:
            decoded_content = base64.b64decode(encoded_content)
            self.logger.info("Successfully decoded POD content")
            return decoded_content
        except Exception as e:
            self.logger.error(f"Failed to decode POD content: {str(e)}")
            raise
