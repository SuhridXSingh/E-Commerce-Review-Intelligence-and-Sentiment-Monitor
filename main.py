import encodings
import encodings
import encodings
import encodings
import encodings
import encodings
import encodings
import encodings
from config.logger import setup_logger
from core.exceptions import BaseAppException, APIConnectionError
from collectors.api_collector import APICollector
from collectors.scraper import WebScraper
from bs4 import BeautifulSoup

#MILESTONE1 SMOKE TEST:

s = setup_logger("app")
s.info("Application Starting...")

# try:
#     raise APIConnectionError()
# except BaseAppException as e:
#     s.error(f"Caught error: {e}")

# s.info("Program continues running...")

#MILESTONE2 SMOKE TEST:

# mock_item = {
#     "id": 1,
#     "title": "Fjallraven Backpack",
#     "category": "men's clothing",
#     "rating": {"rate": 3.9, "count": 120},
#     "description": "Your perfect pack for everyday use."
# }

# collector = APICollector("https://fakestoreapi.com/products")

# # try:
# #     raw_data = collector.collect()

# #     for item in raw_data:
# #         review = collector.parse_review(item)
# #         print(review)
# # except BaseAppException as e:
# #     s.error(f"Caught Error: {e}")

# mock_rev = collector.parse_review(mock_item)

# print("\n--- Testing Model Output ---")
# print("Str representation:", mock_rev)
# print("Dictionary export :", mock_rev.to_dict())
# print("Rating property   :", mock_rev.rating)

with open("test.html", "r", encoding="utf-8") as f:
    html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")
    card = soup.find("div", class_="review-card")
    scraper = WebScraper("local-test")
    scraped_review = scraper.parse_review(card)
    print(f"{scraped_review} {scraped_review.to_dict()}")

    


