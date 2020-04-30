
#@author Neel Patel
#@file BackendAndValidation.py

from firebase import firebase

#constants for dicts
NAME = "Name"
EMAIL = "Email"
FOLLOWING = "Following"
FOLLOWERS = "Followers"
AMOUNT_FOLLOWING = "Amount Following"
AMOUNT_FOLLOWERS = "Amount Followers"
#Firebase to store all information about users
firebase_url = "your_firebase_url_here"
database = firebase.FirebaseApplication(firebase_url, None)
#Table URL
table = "/Users/"

#Indent declaration
INDENT = "   | "

def print_all_users():
    all_users = database.get(table, None)
    if all_users is None:
        print("Database is empty!")
    else:
        for user,data in all_users.items():
            print(user)
            for prop, value in data.items():
                if prop[0] != "-":
                    if prop == FOLLOWERS or prop == FOLLOWING:
                        print(INDENT + prop + ": ")
                        for items in data[prop]:
                            print("   | ---> " + items)
                    else:
                        print(INDENT + str(prop) + " : " + str(value))
            print()

def get_hashed_user(name, email):
    return str(name + " (" + email[0:email.index("@")] + ")")

def _user_exists(email):
    all_users = database.get(table, None)
    if all_users is None:
        return False
    for data,value in all_users.items():
        if email == value[EMAIL]:
            return True
    return False

def _post_dict(uid, data):
    database.put(table + uid, NAME, data[NAME])
    database.put(table + uid,EMAIL, data[EMAIL])
    database.put(table + uid,FOLLOWING, data[FOLLOWING])
    database.put(table + uid,FOLLOWERS, data[FOLLOWERS])
    database.put(table + uid,AMOUNT_FOLLOWING, data[AMOUNT_FOLLOWING])
    database.put(table + uid,AMOUNT_FOLLOWERS, data[AMOUNT_FOLLOWERS])

def create_user(name, email):
    if _user_exists(email):
        print("User with the email " + str(email) + " is already in the database.")
        return True
    else:
        new_user = {NAME: name, EMAIL: email, FOLLOWING: {} , FOLLOWERS: {}, AMOUNT_FOLLOWING: 0, AMOUNT_FOLLOWERS: 0}
        database.post(table + get_hashed_user(name, email), name)
        _post_dict(get_hashed_user(name, email), new_user)

def delete_user(name, email):
    if _user_exists(email):
        database.delete(table + get_hashed_user(name, email), None)
        print("User : " + name + " with email : " + email + " deleted from the database")
    else:
        print("User does not exist!")

def follow(source, destination):
    user_keys = database.get(table, None).keys()
    if source not in user_keys:
        print(source + " does not exist!")
    elif destination not in user_keys:
        print(destination + " does not exist!")
    else:
        source_url = table + source + "/"
        destination_url = table + destination + "/"
        if database.get(source_url + FOLLOWING, None) is not None and destination in database.get(source_url + FOLLOWING, None):
            print(source + " is already following " + destination)
            return False
        database.put(source_url + FOLLOWING, destination, destination)
        database.put(destination_url + FOLLOWERS,source, source)
        database.put(source_url, AMOUNT_FOLLOWING, len(database.get(source_url + FOLLOWING, None).keys()))
        database.put(destination_url, AMOUNT_FOLLOWERS, len(database.get(destination_url + FOLLOWERS, None).keys()))

def unfollow(source, destination):
    user_keys = database.get(table, None).keys()
    if source not in user_keys:
        print(source + " does not exist!")
    elif destination not in user_keys:
        print(destination + " does not exist!")
    else:
        source_url = table + source + "/"
        destination_url = table + destination + "/"
        if database.get(source_url + FOLLOWING, None) is None or destination not in database.get(
                source_url + FOLLOWING, None):
            print(source + " is not following " + destination)
            return False
        database.delete(source_url + FOLLOWING, destination)
        database.delete(destination_url + FOLLOWERS, source)
        if FOLLOWING not in database.get(source_url,None).keys():
            database.put(source_url, AMOUNT_FOLLOWING,0)
        else:
            database.put(source_url, AMOUNT_FOLLOWING, len(database.get(source_url + FOLLOWING, None).keys()))
        if FOLLOWERS not in database.get(destination_url, None).keys():
            database.put(destination_url, AMOUNT_FOLLOWERS, 0)
        else:
            database.put(destination_url, AMOUNT_FOLLOWERS, len(database.get(destination_url + FOLLOWERS, None).keys()))