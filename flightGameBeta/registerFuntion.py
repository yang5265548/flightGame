import random
import public_function.DatabaseConnection as function
import public_function.passwordtool as sha1
# 注册时让用户输入用户名密码，返回用户名和加密后的密码

def register():
    username=input("please enter your username: ")
    checkResult=function.getResultList(f"select * from flight_game.user_flight_game where username = '{username}'")
    while checkResult !=None:
        username=input("username has exsit,please enter username again: ")
        checkResult=function.getResultList(f"select * from flight_game.user_flight_game where username = '{username}'")

    password=input("please enter your password: ")
    passwordCheck=input("please enter your password again: ")
    while password!=passwordCheck:
        password=input("the pass word is not same,please enter password again: ")
        passwordCheck = input("please enter your password again: ")
    # 此时已经已经获得用户名，密码，
    print(username,password,passwordCheck)
    # 给用户密码进行加密
    passwordSha1=sha1.sha1password(password)
    insertsql=f"insert into flight_game.user_flight_game(username,password) values('{username}','{passwordSha1}')"
    # 讲用户名和加密后的密码插入数据库
    function.oprateData(insertsql)
    # 将用户名和密码插入dic 并返回，这个返回值可以删除，目前还没确定
    user={"username":username,"password":passwordSha1}
    return user


# register()
#     # if checkResult==None:
#     #     ...
#     # else:



# 从查出的该国家机场列表中，随机取出十个城市
def get10AirportsFromCountryList(countryList):
    tenAirportsList=random.sample(countryList,10)
    print(tenAirportsList)

    airportlist=[]
    # 拿到10个机场的list
    for list in tenAirportsList:
        airportlist.append(list[2])
    print(airportlist)
    return airportlist


# 将十个机场随机存入from，to
def randAirportFromTo(airportlist):
    fromlist=random.sample(airportlist,5)
    tolist = []
    fromToList=[]
    fromToDict={}
    for list in airportlist:
        if list not in fromlist:
            tolist.append(list)
    for i in range(5):
        fromToDict["from"]=fromlist[i]
        fromToDict["to"]=tolist[i]
        fromToList.append(fromToDict)
    return fromToList
    # print(fromlist)
    # print(tolist)
    # print(airportlist)
    # print(fromToList)


# 查询出用户国家的所有未关闭的机场，并打乱顺序，将所有信息插入list，并返回该list
def checkCountryList(countryName):
     sql=" select airport_id,airport_ident,airport_name,airport_type,lat_deg,lon_deg,country_name,iso_country,fuel_price from airport_flight_game_copy1 where country_name= '"+countryName+" ' and airport_type != 'closed' order by rand() limit 10"
     result=function.getResultList(sql)
     countryList=[]

     # dict={}
     if result !=None:
       for row in result:
           print(row)
           countryList.append(row)
           # 以下代码用来将list存入dict
           # dict["airport_id"]=row[0]
           # dict["airport_ident"]=row[1]
           # dict["airport_type"]=row[2]
           # dict["lat_deg"]=row[3]
           # dict["lon_deg"]=row[4]
           # dict["country_name"]=row[5]
           # dict["iso_country"]=row[6]
           # dict["fuel_price"]=row[7]

     return countryList


list=checkCountryList("United States")
tenairportslist=get10AirportsFromCountryList(list)
randAirportFromTo(tenairportslist)
# print("-----------------------")
# for i in list:
#     print(i)

