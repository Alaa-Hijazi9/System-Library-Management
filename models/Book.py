from .User import User
from .LibraryItem import LibraryItem
from .Reservable import Reservable
from exceptions import ItemAlreadyReservedError

class Book (LibraryItem,Reservable):#يمثل كتاب داخل المكتبة 
    def __init__(self,item_id, title, author,genre:str):
        super().__init__(item_id,title, author)# الاي دي زي لما نحكي انه هذا الكتاب رقمه 2
        self.genre=genre #الخاصية هاي خاصة بالكتاب 
        #نوع الكتاب (خيال, تاريخ,علووم...)
        self.reserved = False# نفترض انه الكتاب  مش محجوز 
    # item_id هو رقم تسلسلي او معرف داخلي مو لازم يكون ظاهر دائما للمستخدم  
    def display_info(self):
        print(f"Book ID: {self.item_id} - Title: {self.title} by {self.author} - Genre: {self.genre} - Available: {self.available}")

        #self.available لانه انا عامل انه يورث من ابوه الصفات المشتركة فهاي موجودة باال انت 
        #كيف يعني ؟؟؟
        #super().__init__(item_id,title, author) لما هان انا جيت حكيتله
        #جيبلي من ابوي دالة الانت يعني الكونستراكتور وابعتله هاي القيم
        #لانه فيه انه يستقبل قيم وحيتم بعث هاي القيم اله
        #لكن المتغير افيلبل اله قيمة فما بنحط انه يستقبل قيمة
        #فبتم توريثها من ابوه زي ما حكينا هو ورثها من ابوه من خلال السوبر
        #فبتم توريث دالة الانت باللي فيها
        
    def check_availability(self):
        return self.available

    def reserve(self,user:User):
        if not self.reserved : #اذا الكتاب مش محجوز روح احجزلي ياه وعدلي على قيمته
            self.reserved =True
            self.available = False#وهان بعدل على قيمتها وبخليها ترو انه محجوز وراح يظهر رسالة بالحجز
            print(f"The Book has been booked '{self.title}' by {user.name}") 
            # حطينا الاسم مشان يتم حفظ الكتاب للمستخدم انه مستعيره
            #name هان ارسلت للميثود اوبجيكت من كلاس اليوزر واخذت منه المتغير 
            #user.name انا بجيب من داخل الاوبجت اللى هو يوزر بنجيب متغير النيم 
            
            #هان لو انا حجزت الكتاب لكن ضلت الافليبل انه متاح يعني بيقدر حدا يحجزه وهان 
            #لازم نمنع الاستعارة بعد الحجز 
            #المقصد
            #أنت تغيّر فقط حالة reserved = True
            #لكن الافيلبل (اي هل يمكن استعارته ) تظل تروو 
            
        else:
            raise ItemAlreadyReservedError ("This Book is already booked")
            
    def to_dict (self):# to_dict()    لحفظ بيانات الكتب.
        return { "type": "Book",
        "item_id":self.item_id,
        "title": self.title,
        "author":self.author,
        "genre": self.genre,
        "available":self.available,
        "reserved":self.reserved,
    }