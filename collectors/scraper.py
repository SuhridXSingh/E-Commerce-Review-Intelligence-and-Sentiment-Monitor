from core.models import Review
from collectors.base import BaseCollector
from core.exceptions import BaseAppException, ScrapingError
import requests
from bs4 import BeautifulSoup

class WebScraper(BaseCollector):
    def __init__(self, target_url, *args, **kwargs):
        super().__init__("scraper", **kwargs)
        self.target_url = target_url
    
    def collect(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        try:
            response = requests.get(self.target_url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup.find_all("div", class_="review-card") # finds all div tags in the html page with the class review-card.
            else:
                raise ScrapingError(f"HTTP Status: {response.status_code}")
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error: {e}")
            raise ScrapingError("Request failed", str(e))

        except BaseAppException as e:
            self.logger.error(f"Error: {e}")
            raise

    def parse_review(self, raw_data):
        title_elem = raw_data.find("h3", class_="product-name")
        pd_name = title_elem.get_text(strip=True) if title_elem else "Unknown Product"

        author_elem = raw_data.find("span", class_="reviewer-name")
        reviewer_name = author_elem.get_text(strip=True) if author_elem else "Anonymous"

        rate_elem = raw_data.find("span", class_="rating")
        try:
            rating = float(rate_elem.get_text(strip=True))
        except Exception as e:
            rating = 0.0
        
        text_elem = raw_data.find("p", class_="review-text")
        review_text = text_elem.get_text(strip=True) if text_elem else ""

        rev_id = raw_data.get("data-id")

        return  Review(
           rev_id=rev_id,
           pd_name=pd_name,
           rev_name=reviewer_name,
           rating=rating,
           rev_text=review_text,
           source="scraper"
       )
