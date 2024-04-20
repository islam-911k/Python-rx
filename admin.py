import re
from datetime import datetime

# assuming this list is our database(DB)
users_db = []


def login():
    print("===== Welcome Admin! =====")
    while True:
        passwd = input("Login password: ")
        if passwd == 'admincc':
            dashboard()
        else:
            print("Incorrect password")


def dashboard():
    while True:
        operations = ['exit', 'add user', 'edit user', 'delete user', 'list all users', 'search user']
        for operation in operations:
            print(f"press {operation[0:2]} to ===> {operation} ")
        command = input("chose an operation: ")
        if command == operations[0][0:2]:
            print("===== logged out! ===== \n")
            login()
        elif command == operations[1][0:2]:
            add_user()
        elif command == operations[2][0:2]:
            update_user()
        elif command == operations[3][0:2]:
            delete_user()
        elif command == operations[4][0:2]:
            get_users()
        elif command == operations[5][0:2]:
            search_user()
        else:
            print("+++++++ That's not valid +++++++")


def add_user():
    user_info = {
        "Id": input("user ID (numbers and chars only): "),
        "username": input("User fullname (chars only): "),
        "join_date": datetime.today().strftime("%Y/%m/%d %H:%M"),
        "address": input("Address (numbers and chars only): "),
        "phone": input("Phone Ex (+123 456 789 112) : "),
        "email": input("Email (example@gmail.com) : "),
    }
# calling the function to check if there is a user exists
# with same information to prevent future problems
    if id_phone_email_validation(users_db,user_info["Id"],user_info["phone"],user_info["email"]):
        print("+++++ user exist +++++")
        return False
    else:
        if user_info_validation(user_info):
            users_db.append(user_info)
            print("+++++ added successfully +++++")

        else:
            print("+++++ User not added, due to invalid input +++++")
        return True

# function checks if one of these data
# already belongs to an existing user
def id_phone_email_validation(users,new_id,new_phone,new_email):
    for user in users:
        if user["Id"] == new_id :
            print(f"This ID {user['Id']} Already exist")
            return True
        elif user["phone"] == new_phone:
            print(f"This Number {user['phone']} Already exist")
            return True
        elif user["email"] == new_email:
            print(f"This Email {user['phone']} Already exist")
            return True
    return False

# using reEx to validate admin input
# to prevent mistype data
def user_info_validation(input_values):
    for key, value in input_values.items():
        if key == "phone":
            if not re.match(r"^\+\d{3}\s\d{3}\s\d{3}\s\d{3}$", value):
                print(f"+++++++ {key} invalid input. follow this pattern: +123 456 789 112  +++++++")
                return False
        elif key == "email":
            if not re.match(r"^[a-zA-Z0-9_]+@gmail\.com$", value):
                print(f"+++++++ {key} not valid, pattern: example@gmail.com +++++++")
                return False
        elif key == "username":
            if not re.match("^[a-zA-Z\s]+$", value):
                print(f"+++++++ name '{key}' not valid +++++++")
                return False
        elif key == "Id":
            if not re.match("^[a-zA-Z0-9]+$", value):
                print(f"+++++++ {key} invalid. ID is combination between Chars and Numbers Only+++++++")
                return False
        elif key == "address":
            if not re.match(r"^[a-zA-Z0-9_.+-]+$", value):
                print(f"+++++++ {key} not valid+++++++")
                return False
    return True


def get_users():
    if len(users_db) != 0:
        for user in users_db:
            print(
                f" ==> ID: {user['Id']}  ==> Name: {user['username']}  ==> Joined: {user['join_date']}  ==> Address: {user['address']}  ==> Phone: {user['phone']}  ==> Email: {user['email']}")
    else:
        print("+++++++ List is empty +++++++")


def search_user():
    if len(users_db) != 0:
        search = input("search name:")
        if not re.match("^[a-zA-Z]+$", search):
            print(f"+++++++ This {search} is invalid input +++++++")
            return False
        else:
            for user in users_db:
                if search == user["username"]:
                    print(
                        f" found ID: {user['Id']} Name: {user['username']} Joined: {user['join_date']} Address: {user['address']} Phone: {user['phone']} Email: {user['email']}")
                elif search != user["username"]:
                    print(f"{search} not found")
    else:
        print("+++++++ List is empty +++++++")

# to update user info with a strict rules
# to prevent any mismatch data
def update_user():
    success_message = "Updated successfully"
    rejection_message = "rejected update, due to invalid input"
    if len(users_db) != 0:
        user_id = input("user Id: ")
        print('chose what to update [ username address phone email ]')
        command = input("I chose: ")
        for user in users_db:
            if user_id == user["Id"]:
                if command == "username":
                    new_name = input(f"current => {user['username']} new =>")
                    validate_new_name = re.match("^[a-zA-Z\s]+$", new_name)
                    if not validate_new_name:
                        print(rejection_message)
                        return False
                    else:
                        print(success_message)
                        user['username'] = user["username"].replace(user["username"], new_name )
                elif command == 'address':
                    new_address = input(f"current => {user['address']} new =>")
                    if not re.match(r"^[a-zA-Z0-9_.+-]+$", new_address):
                        print(rejection_message)
                        return False
                    else:
                        print(success_message)
                        user['address'] = user["address"].replace(user["address"],new_address)
                elif command == 'phone':
                    new_phone = input(f"current => {user['phone']} new =>")
                    validate_new_phone = re.match(r"^\+\d{3}\s\d{3}\s\d{3}\s\d{3}$", new_phone)
                    if not validate_new_phone:
                        print(rejection_message)
                        return False
                    else:
                        print(success_message)
                        user['phone'] = user["phone"].replace(user["phone"], new_phone)
                elif command == 'email':
                    new_email = input(f"current => {user['email']} new =>")
                    validate_new_email = re.match(r"^[a-zA-Z0-9_]+@gmail\.com$", new_email)
                    if not validate_new_email:
                        print(rejection_message)
                        return False
                    else:
                        print(success_message)
                        user['email'] = user["email"].replace(user["email"],new_email )
                print(
                    f"ID: {user['Id']} Name: {user['username']} Joined: {user['join_date']} Address: {user['address']} Phone: {user['phone']} Email: {user['email']} Updated on {datetime.today().strftime('%Y/%m/%d %H:%M')}")
    else:
        print("+++++++ List is empty +++++++")


def delete_user():
    if len(users_db) != 0:
        dele = input('user id ')
        for user in users_db:
            if user["Id"] == dele:
                users_db.remove(user)
                print(
                    f"ID: {user['Id']} Name: {user['username']} Joined: {user['join_date']} Address: {user['address']} Phone: {user['phone']} Email: {user['email']} deleted on {datetime.today().strftime('%Y/%m/%d %H:%M')}")
            elif user["Id"] != dele:
                print(f"{dele} not found")
    else:
        print("+++++++ List is empty +++++++")


# entre point ( program starts from here)
login()
