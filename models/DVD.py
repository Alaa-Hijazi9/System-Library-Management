from .LibraryItem import  LibraryItem
from .Reservable import Reservable
from .User import User
from exceptions import ItemAlreadyReservedError

class DVD (LibraryItem,Reservable):#يمثل  قرص داخل المكتبة 
    def __init__(self,item_id, title, author,duration):
        super().__init__(item_id,title, author)
        self.duration=duration#مدة التشغيل للفلم بالدقائق 
        #يعني مدة الفيلم او المحتوى ب
        # dvd
        self.reserved = False
        
    def display_info(self):
        print(f"DVD ID: {self.item_id} - Title: {self.title} by {self.author} - Duration: {self.duration} - Available: {self.available}")

    def check_availability(self):
        return self.available
    
    def reserve(self,user:User):
        if not self.reserved :
            self.reserved =True
            self.available = False
            print(f"The DVD has been booked '{self.title}' by {user.name}") 
        else:
            raise ItemAlreadyReservedError ("This DVD is already booked")
        
    def to_dict (self):
        return { "type": "DVD",
        "item_id": self.item_id,
        "title": self.title,
        "author": self.author,
        "duration": self.duration,
        "available": self.available,
        "reserved": self.reserved,
    }