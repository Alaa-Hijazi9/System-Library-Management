from .LibraryItem import  LibraryItem
class Magazine (LibraryItem): #يمثل مجلة داخل المكتبة ما بنقدر نحجزها 
    def __init__(self,item_id, title, author,issue_number):
        super().__init__(item_id,title, author)
        self.issue_number=issue_number #رقم العدد للمجلة مثلا العدد رقم 5
        self.available = True
        
    def display_info(self):
        print(f"Magazine ID: {self.item_id} - Title: {self.title} by {self.author} - Issue number: {self.issue_number} - Available: {self.available}")
        
    def check_availability(self):
        return self.available
    
    def to_dict (self):
        return { "type": "Magazine",
        "item_id":self.item_id,
        "title": self.title,
        "author":self.author,
        "issue_number":self.issue_number,
        "available": self.available,
    }