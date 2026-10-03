from config.logger import setup_logger
class BaseCollector:
    def __init__(self, source_name, **kwargs):
        self.source_name = source_name
        self.logger = setup_logger(self.source_name)
        self.config = kwargs #Stores Everything else as a dict 
    
    def collect(self):
        raise NotImplementedError
    
    def parse_review(self, raw_data):
        raise NotImplementedError