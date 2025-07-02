# from .LibraryItem import LibraryItem
# class User : #يمثل الشخص اللى بيستعيراو بيحجز عناصر من المكتبة
#     def __init__(self,user_id:int,name:str,email: str):
#         self.user_id=user_id
#         self.name=name
#         self.email = email
#         self.borrowed_items=[] # ليستة بالعناصر اللى استعارها المستخدم
        
#     def borrow_item(self,item:LibraryItem):
#         if item not in self.borrowed_items:#شرط يتأكد إن المستخدم ما استعار نفس العنصر من قبل 
#             self.borrowed_items.append(item)#مثل ما حكينا هان او ما عملت ليسته بدي اعمل اضافة فيها
#             item.available=False #وبعدها بخلي العنصر مش متاح وانه خلص انحجز
    
#     def return_item (self,item:LibraryItem):#  دالة لارجاع عنصر بنشيله من القائمة ونرجع العنصر كانه متاح يعني بتقدر تحجزه
#         if item in self.borrowed_items:
#             self.borrowed_items.remove(item)
#             item.available=True# بخلي العنصر متاح
            
            
            
#     def to_dict (self):
#         # # تحويل المستخدم لقاموس لحفظه في ملف JSON
#         # json بتحول الكائن الى ديكنشري حتى يتمكن من تخزينه بصيغة
#         return {
#         "user_id":self.user_id,
#         "name": self.name,
#         "email": self.email,
#         "borrowed_items": [item.item_id for item in self.borrowed_items]
#     }


import array
arr=array.array('i',[0]*6)
