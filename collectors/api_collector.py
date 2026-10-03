from core.models import Review
from core.exceptions import BaseAppException
from core.exceptions import APIConnectionError
import requests
from collectors.base import BaseCollector
class APICollector(BaseCollector):
    def __init__(self, base_url, *args, **kwargs):
        super().__init__("api", **kwargs)
        self.base_url = base_url
    
    def collect(self):
        try:
            response = requests.get(self.base_url, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                raise APIConnectionError(f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            raise APIConnectionError("Request failed", str(e))
        except BaseAppException as e:
            self.logger.error(f"Caught Error: {e}")
            raise
    
    def parse_review(self, raw_data):
        return Review(
            rev_id=raw_data["id"],
            pd_name=raw_data["title"],
            rev_name=raw_data["category"],
            rating=raw_data["rating"]["rate"],
            rev_text=raw_data["description"],
            source="api"
        )

