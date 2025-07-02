import json
from .LibraryItem  import LibraryItem
from .Reservable import Reservable
from .Book import Book
from .DVD import DVD
from .Magazine import Magazine
from .User import User
from exceptions.ItemAlreadyReservedError import ItemAlreadyReservedError
from exceptions.ItemNotAvailableError  import ItemNotAvailableError
from exceptions.ItemNotFoundError import ItemNotFoundError
from exceptions.UserNotFoundError import UserNotFoundError
class Library: #بجمع كل العناصر والمستخدمين وبتعامل مع كل العمليات 
    def __init__(self):
        self.items=[]
        self.users=[]
    def add_item(self,item):
        self.items.append(item)
        print(f"Added item '{item.title}' to the library.")
        
    def add_user(self,user):
        self.users.append(user)
        print(f"Added user '{user.name}' to the library.")
    # في عملية اضافة مستخدم او عنصر 
    # ليه ما استخدمنا الطريقة هاي انه اضيف البيانات مباشرة للملف 
    # def add_item(self,item):
    #     with open ("items.json","a") as f :
    #         f.write(item)
    #a احنا هان بنستخدم وضع الاضافة 
    #json هان بيروح بيضيفلي العنصر بشكل مباشر لملف ال 
    #  عبارة عن انك بتحول البيانات لقائمة json لو عملتها بيخرب تنسيق الملف لانه ملف 


    # IDإيجاد عنصر حسب 
    def find_item(self, item_id):
        for item in self.items: # الفكرة انه انا بخزن في الليست بتبعتي كائنات 
            #يعني الايتم بالبداية راح تمسك اوبجكت من القائمة 
            #كل اوبجكت من القائمة اله خصائص وميثود
            if item.item_id == item_id:
                return item
        raise ItemNotFoundError("Item Not Found ")

    # IDإيجاد مستخدم حسب 
    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise UserNotFoundError("User Not Found.")
    #عملية الحذف 
# طيب لو روحت عملت سواء في العنصر او المستخدم 
    # def remove_item(self,item:LibraryItem):
    #         self.items.remove(item)
    #هان انا بحذف عنصر باستخدام الكائن نفسه مش بالمعرف وهان ممكن يسبب مشكلة عندك
    #بنعمل حذف باستخدام الاي دي 
    #علشان هيك عملت بالدالتين اللى فوق ايجاد مستخدم وعنصر عن طريق الاي دي 
    
    def remove_item (self,item_id):
        item=self.find_item(item_id)
        #بتاخذ الاي دي 
        #بتروح بتبعته لدالة ايجاد الاي دي تبع العنصر 
        #بتروح بدور عليه بالدالة اذا لقته بترجعه وبتخزنه في البارميتر ايتم وبتعمله ازالة
        self.items.remove(item)
        print(f"Removed item '{item.title}' from the library.")
        
    def remove_user (self,user_id):
        user=self.find_user(user_id)
        self.users.remove(user)
        print(f"Removed user '{user.name}' from the library.")
        
    
    # استعارة عنصر حسب الاي دي 
    def borrow_item(self, user_id, item_id):
        user = self.find_user(user_id)
        item = self.find_item(item_id)

        if not item.check_availability():
            #هلا هان المستخدم يستعير عنصر 
            #بندور على المستخدم والعنصر اللى بدهم يستعيروا 
            #بنشيك اذا العنصر متاح (مش مستعار )
            #اذا مش متاح نرمي خطأ
            #اذا متاح نخليه مستعار ونطبع رسالة
            # يعني لو التشيك كان تروو 
            # نفي التروو فولس يعني مش متاح 
            # ما تحقق الشرط بطلع من الاف 
            #وبروح بيستعيره 
            raise ItemNotAvailableError("Item Not Available")
        if getattr(item, 'reserved', False):  ##
            #هذا السطر بتاكد اذا خاصية الريسيرفد موجود بالايتم
            #اذا كانت موجودة وقيمتها تروو يمنع الاستعارة
            #اذا كانت غير موجودة بيرجع قيمة افتراضية فولس وما يمنعها
            #هات خاصية الريسيرفد من الايتم اذا موجودة بيرجع تروو 
            #اما اذا مش موجودة بيرجع فولس 
            raise ItemAlreadyReservedError("This item is reserved and cannot be borrowed.")
        user.borrow_item(item)#بضيفلي ياه على قائمة الاستعارة الخاصة بالمستخدم 
        print(f" '{item.title}' has been borrowed by {user.name}.")
        
        # إرجاع عنصر
        #نفس الشي قبل بنشوف مين العنصر ومين المستخدم وبنرجع العنصر(بيصير متاح من جديد)
    def return_item(self, user_id, item_id):
        user = self.find_user(user_id)
        item = self.find_item(item_id)
        user.return_item(item)
        print(f" '{item.title}' has been returned by {user.name}.")
        
    # حجز عنصر
    #بنشوف اذا العنصر بيدعم الحجز(عنده دالة reserve())
    def reserve_item(self, user_id, item_id):
        user = self.find_user(user_id)
        item = self.find_item(item_id)
#هل الايتم عنده دالة ريسيرف اذا اه بنعمل حجز اذا لاء نرمي خطا
        if hasattr(item, 'reserve'):#ببتاكد الدالة هاي 
            #اذا الكائن فيه دالة معينة قبل ما نستدعيها 
            item.reserve(user)
        else:
            raise ItemNotFoundError("This type of item cannot be found")
# وتحويلها الى كائنات jsonتحميل العناصر من ملف 
#هاي الكائنات مثل الكتاب والقرص والمجلة 
    def load_items_from_file(self, filename): # بستقبل الملف اللى انا بعته من خلال الاستدعاء 
        try:# مشان لو ظهرت عندي مشكلة يقدر يعاجلها سواء لو مفيش ملف ومايتوقف البرنامج
            with open(filename, 'r') as f:# بيروح بيفتح الملفو  وبيقرا من هذا الملف 
                data = json.load(f)
                # بتأشر على الملف  fارسلت للدالة ال 
                #وظيفتها لدالة 
                # JSONتحول نص الـ  
                ## الموجود داخل الملف إلى كائنات بايثون (مثل: قوائم، قواميس، أرقام، نصوص...)
                #حتى لو شكل البيانات يشبه كائنات بايثون، بايثون ما بتعامل معها ككائنات إلا بعد تحويلها.
                #لانه شكل الملف بالديكشنري والليست بس مش كائنات يعني لازم نحولهم 
                #بس لما نحولهم بيطلعوا نفس الشكل 
                
                if not data:#بتفحص لو الملف كان فارغ
                    print("The file is empty. No users loaded.")
                    
                for item_data in data:#هان بتلف على كل كائن موجود عندي من الملف لانه حولناهم لكائنات 
                    #بيمسك اول كائن من الملف 
                    item_type = item_data.get("type")# item_dataمن القاموس "type"بتاخذ قيمة المفتاح 
                    #هلا الايتم دوت داتا هي صارت اوبجيكت 
                    #فبمسك الاوبجت وبدي اجيب منه التايب يعني يرجع التايب      
#وظيفة الميثود هاي 
#لو المفتاح تايب موجود ترجع قيمته مثلا بوك او ديفيدي
#.لو المفتاح مش موجود ترجع نون بدل ما يطلع خطا

                    #اذا نوع العنصر كان بوك افعل كذا..
                    if item_type == "Book":
                            item = Book(# بعمل كائن جديد من كلاس البوك وبعطيه البيانات اللى قراناها من ملف الجيسون
            #هدول القيم ماخوذين من ملف الجيسون وبيمثلوا الخصائص الخاصة بالكتاب 
            #بيتم تمريرهم الى الكلاس البوك
            #Book(item_id, title, author, genre)
            #اي قيمة بخزنهم بنبعتوا الى 
            #item = Book(1, "Python Basics", "Alaa Hijazi", "Programming")
            #كانه بنحكي من كل الاوبجكت اللى نوعه بوك جيبلي الايتم اي دي وكذالك بالكل..
                            item_data["item_id"],
                            #راح يجيب الايتم اي دي من ملف الجيسون ويبعته للكلاس
                            #القاموس كلمة ومفتاح 
                            #  "item_id"  قيمة المفتاح item_data هان بنطلب من القاموس 
                            #وهكذاااا
                            item_data["title"],
                            item_data["author"],
                            item_data["genre"]    
                    )

                    elif item_type == "DVD":
                        item = DVD(
                            item_data["item_id"],
                            item_data["title"],
                            item_data["author"],
                            item_data["duration"]
                    )

                    elif item_type == "Magazine":
                        item = Magazine(
                            item_data["item_id"],
                            item_data["title"],
                            item_data["author"],
                            item_data["issue_number"]
                    )

                    else:
                        print(f"Unknown item type: {item_type}, skipping.")
                        continue
                    
                    self.items.append(item)#بنضيف العنصر الى قائمة العناصر اللى موجودة في المكتبة وهنا بنخزن العنصر الجديد

        except FileNotFoundError:
            print("File not found:", filename)
            
        except json.JSONDecodeError:# الملف ممكن يكون فيه خطا في التنسيق يعني مكتوب غلط
            print("Error decoding JSON from file:", filename)

    def load_users_from_file(self, filename):
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                if not data:
                    print("The file is empty. No users loaded.")
                    
                for user_data in data:
                    user = User(
                        user_data["user_id"],#حتى اجيب قيمة من القاموس والقيمة اللى بجيبها ببعتها للكلاس 
                        user_data["name"],
                        user_data.get("email", "")  # لو الإيميل غير موجود افترض فارغ
                )
                # مؤقتًا نخزن أرقام العناصر
                    user.borrowed_items = user_data.get("borrowed_items", [])
                #بنحاول نجيب قيمة المفتاح  بوروو ايتمز من القاموس يوزر داتا
                #اذا المفتاح بوروو ايتمز موجود بنرجع قيمته فعادة تكون قائمة تحتوي على العناصر اللى استعارهم المستخدم
                #اما اذا المفتاح غير موجود بنرجع قائمة فارغة كقيمة افتراضية مشان ما يظهر ايرور
                    self.users.append(user)#راح تضيف المستخدم على قائمة المستخدمين 
                    
        except FileNotFoundError:
            print("Users file not found.")
            
        except json.JSONDecodeError:
            print("Error decoding users.json.")
#عند تحميل بيانات المستخدمين من ملف زي الجيسون احيانا بنخزن رقم العنصر 
#الاي دي فقط مش الكائن نفسه 
#مثلا لما نحكي انه المستخدم الاء استعار عناصر ارقامهم 2و3و4
#   هان ال2 هي كرقم العنصر ولكن هان احنا خزناه كرقم عنصر ولكن 
#يعني هل 2 هل هي كتاب ولا مجلة ولا قرص 
#لو كانت كتاب فانت اخدت رقم العنصر فقط ما اخدته للكائن كله
#فبنعمل عملية الربط  
      
#الربط بين المستخدمين والعناصر المستعارة 
#عند تحميل بيانات المستخدمين ملف الجيسون عادة بنحصل على قائمة معرفات العناصر
#الاي دي اللى استعارها كل مستخدم مثل 1و2و3
#لكن هاي مجرد ارقام وليس كائنات حقيقية في البرنامج
#الربط يعني 
#نحول هاي الارقام الاي دي الى كائنات الليبرري ايتم حقيقية موجودة 
#داخل النظام ونضيفها لقائمة البوروو ايتمز لكل مستخدم
# الربط يحول البيانات المخزنة الاي دي #
# إلى كائنات حقيقية ترتبط بالمستخدم داخل النظام.
    def link_borrowed_items(self):
        for user in self.users:#نمر على كل مستخدم موجود في النظام.
        # نسخ الأرقام مؤقتًا
            borrowed_ids = list(user.borrowed_items)#اخذت كل الارقام اللى استعارهم المستخدم وخزنتها بليست 
            user.borrowed_items = []#بعدها فرغت الليست هاي 
#فلو ما فرغنا القائمة، وبدأنا نضيف كائنات داخلها، 
# راح تصير القائمة مخلوطة بين أرقام وكائنات! 
# وهذا ممكن يعمل مشاكل لاحقًا.
#يعني زي كاني اخدت نسخة من الارقام وبعدها فرغتها حتى نرجع نضيف فيها كائنات
            for item_id in borrowed_ids:
                try:
                    item = self.find_item(item_id)#نبحث عن كائن العنصر باستخدام الاي دي
                    user.borrow_item(item)#بيضيف الكائن الى قائمة العناصر المستعارة
                    #نربط العنصر بالمستخدم (أي نخليه يستعيره فعليًا)
                    
                except ItemNotFoundError:
                    print(f"Item ID {item_id} for user {user.name} not found.")

    def save_items_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([item.to_dict() for item in self.items], f, indent=4)
#هاي الدالة الديمب 
#تحول البيانات البايثون القوائم والقواميس الى نص الجيسون وتخزينها في ملف 
#بتاخذ 3 معاملات 
#المعامل الاول الاوبجيكن كائن الداتا اللى بدك تحوله لجيسون مثلا قائمة من القواميس 
#fp 
#ملف مفتوح للكتابة هو المكان اللى راح تكتب فيه البيانات بصيغة جيسون
#الاندينت اختياري
#عدد المسافات اللى تستخدم لتنسيق الملف بشكل جميل للقراءة 
#الفور انا هيك كل عنصر سيلف ايتمز هو كائن 
    def save_users_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4)
