from models.Library import Library
from models.User import User
from exceptions.ItemAlreadyReservedError import ItemAlreadyReservedError
from exceptions.ItemNotAvailableError  import ItemNotAvailableError
from exceptions.ItemNotFoundError import ItemNotFoundError
from exceptions.UserNotFoundError import UserNotFoundError
def main():#ميثود لتشغيل 
    #راح نروح نعمل اوبجيكت من كلاس الليبرري لانه كل شغلنا موجود عليه
    library = Library()
    #من النسخة اللى عملناها استدعينا الميثود هاي 
    library.load_items_from_file("items.json") #راح اعطيه العناصر من ملف ويبعتها للدالة 
    #يعني الفكرة انه ما ببتع العناصر من انبوت ولكن ببعتها عن طريق ملف وكل البيانات محفوظة فيه
    
    library.load_users_from_file("users.json")
    library.link_borrowed_items()

    while True:
        print("\n Welcome to the Library System")
        print("1. View all available items ")
        print("2. Search item by title or type ")
        print("3. Register as a new user")
        print("4. Borrow an item")
        print("5. Reserve an item")
        print("6. Return an item")
        print("7. Exit and save \n")
        
        choice = input(">>>")

        if choice == "1":
            for item in library.items:
                    item.display_info()

        elif choice == "2":
            keyword = input("Enter item by title or type :").lower()
            found = False
            for item in library.items:
                if keyword in item.title.lower() or keyword in item.__class__.__name__.lower():
                    # keyword in item.__class__.__name__.lower()
                    #(نوع الكلاس تبعه)شرحه انه الايتم دوت كلاس هو نوع الكائن 
                    #item.__class__.__name__ بجيب اسم الكلاس كنص
                    #اللور بنحول الاسم لحروف صغيرة علشان الحساسية 
                    item.display_info()
                    found = True
            if not found:
                print("No items found.")

        elif choice == "3":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            user_id = len(library.users) + 1
            new_user = User(user_id, name, email)
            library.add_user(new_user)
            print(f"User registered successfully with ID {user_id}.")


        elif choice == "4":
            try:
                user_id = int(input("Enter your user ID: "))
                item_id = int(input("Enter the item ID to borrow: "))
                library.borrow_item(user_id, item_id)
            except (ValueError, UserNotFoundError, ItemNotFoundError, ItemNotAvailableError) as e:
                print("Error:", e)

        elif choice == "5":
            try:
                user_id = int(input("Enter your user ID: "))
                item_id = int(input("Enter the item ID to reserve: "))
                library.reserve_item(user_id, item_id)
            except (ValueError, UserNotFoundError, ItemNotFoundError, ItemAlreadyReservedError) as e:
                print("Error:", e)

        elif choice == "6":
            try:
                user_id = int(input("Enter your user ID: "))
                item_id = int(input("Enter the item ID to return: "))
                library.return_item(user_id, item_id)
            except (ValueError, UserNotFoundError, ItemNotFoundError) as e:
                print("Error:", e)

        elif choice == "7":
            try:
                library.save_items_to_file("items.json")
                library.save_users_to_file("users.json")
                print("Data saved. Goodbye!")
            except Exception as e:
                print("Error saving data:", e)
            break

        else:
            print("Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
