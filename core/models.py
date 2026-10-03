from datetime import datetime
class Review:
    def __init__(self, rev_id, pd_name, rev_name, rating, rev_text, source, timestamp=None):
        self._rev_id = rev_id
        self.pd_name = pd_name
        self.rev_name = rev_name
        self.rating = rating
        self.rev_text = rev_text
        self.source = source 
        self._timestamp = timestamp or datetime.now().isoformat()
    
    def __str__(self):
        return f"Review by {self.rev_name} for {self.pd_name}: {self.rating}*"
    
    def __repr__(self):
        return f"Review(id= {self._rev_id}, product= {self.pd_name})"

    def to_dict(self):
        return {
        "Review ID":self._rev_id, 
        "Product":self.pd_name, 
        "Reviewer Name":self.rev_name, 
        "Rating":self.rating, 
        "Review":self.rev_text, 
        "Source":self.source, 
        "Timestamp":self._timestamp
        }

    @property #Read Only Access of the getter method
    def review_id(self):
        return self._rev_id  
