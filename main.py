from config.logger import setup_logger
from core.exceptions import BaseAppException, APIConnectionError

s = setup_logger("app")
s.info("Application Starting...")

try:
    raise APIConnectionError()
except BaseAppException as e:
    s.error(f"Caught error: {e}")

s.info("Program continues running...")
