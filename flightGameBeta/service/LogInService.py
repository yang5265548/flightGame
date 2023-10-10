import hashlib
import  DatabaseConnection as function

def sha1password(password):
    passwordSha1 = hashlib.sha1(password.encode("utf-8")).hexdigest()
    return passwordSha1

def user_exist(username, password):
    while True:
        user_check = sha1password(password)
        username=function.getResultlist(f"select count(0) from user_flight_game where username='{username}' and password='{user_check}'")
        if username is not None:
            return True

        else:
            return False





