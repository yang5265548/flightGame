import hashlib
import flightGameBeta.public_function.DatabaseConnection as function
# 用户密码加密
def sha1password(password):
    passwordSha1 = hashlib.sha1(password.encode("utf-8")).hexdigest()
    return passwordSha1

# 用户密码验证

def checkPassword(username,password):
    flag=True
    while flag:
        checkPassword=sha1password(password)
        password=function.getResultList(f"select password from user_flight_game where username='{username}'")
        if password==checkPassword:
            print("password is right")
            flag=False
        else:
            username=input("password is worng,please enter username again: ")
            password=input("please enter password again: ")

