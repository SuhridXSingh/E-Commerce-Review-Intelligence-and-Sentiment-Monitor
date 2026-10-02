class BaseAppException(Exception):
    def __init__(self, msg, det=None):
        self.msg = msg
        self.det = det
        super().__init__(msg)
    def __str__(self):
        if self.det:
            return f"Error: {self.msg} with details: {self.det}"
        return f"Error: {self.msg}"

class DataCollectionError(BaseAppException):
    def __init__(self, msg="Data Collection Error", det=None):
        super().__init__(msg, det)
class APIConnectionError(DataCollectionError):
    def __init__(self, msg="API Connection Failed", det=None):
        super().__init__(msg, det)
class ScrapingError(DataCollectionError):
    def __init__(self, msg="Data Scraping Failed", det=None):
        super().__init__(msg, det)

class DataStorageError(BaseAppException):
    def __init__(self, msg="Data Storage Error", det=None):
        super().__init__(msg, det)
class DatabaseError(DataStorageError):
    def __init__(self, msg="Database Error", det=None):
        super().__init__(msg, det)
class FileIOError(DataStorageError):
    def __init__(self, msg="File IO Error", det=None):
        super().__init__(msg, det)

class NLPProcessingError(BaseAppException):
    def __init__(self, msg="NLP Processing Error", det=None):
        super().__init__(msg,det)

class ModelError(BaseAppException):
    def __init__(self, msg="Model Error", det=None):
        super().__init__(msg, det)
class ModelTrainingError(ModelError):
    def __init__(self, msg="Model Training Error", det=None):
        super().__init__(msg, det)
class ModelLoadError(ModelError):
    def __init__(self, msg="Model Loading Error", det=None):
        super().__init__(msg, det)
