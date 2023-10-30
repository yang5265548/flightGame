import random
import flightGameBeta.public_function.DatabaseConnection as function
import flightGameBeta.public_function.passwordtool as sha1

# 注册时让用户输入用户名密码，返回用户名和加密后的密码

def register():
    username = input("please enter your username: ")
    checkResult = function.getResultList(f"select * from user_flight_game where username = '{username}'")
    while checkResult != None:
        username = input("username has exsit,please enter username again: ")
        checkResult = function.getResultList(
            f"select * from user_flight_game where username = '{username}'")

    password = input("please enter your password: ")
    passwordCheck = input("please enter your password again: ")
    while password != passwordCheck:
        password = input("the pass word is not same,please enter password again: ")
        passwordCheck = input("please enter your password again: ")
    # 此时已经已经获得用户名，密码，
    # print(username, password, passwordCheck)
    # 给用户密码进行加密
    passwordSha1 = sha1.sha1password(password)
    insertsql = f"insert into user_flight_game(username,password) values('{username}','{passwordSha1}')"
    # 讲用户名和加密后的密码插入数据库
    function.oprateData(insertsql)
    # # 将用户名和密码插入dic 并返回，这个返回值可以删除，目前还没确定
    # user = {"username": username, "password": passwordSha1}
    # return user
    return [username,password];

# 根据首字母列出所有国家,按照机场数量降序排列

def checkAllCountryListStartWith(string):
    quaryAllCountryListSQL = "select DISTINCT(country_name) from airport_flight_game where country_name like '" + string + "%' group by country_name order by count(*) desc"
    result = function.getResultList(quaryAllCountryListSQL)
    allCountryList = []
    if result != None:
        for row in result:
         allCountryList.append(row[0])
    print(allCountryList)
    return allCountryList

# 从国家列表中，让用户选择一个国家，然后输出查询出该国家的所有机场


# 从查出的该国家机场列表中，随机取出十个城市
def get10AirportsFromCountryList(countryList):
    tenAirportsList = random.sample(countryList, 10)
    # print(tenAirportsList)

    airportlist = []
    # 拿到10个机场的list
    for list in tenAirportsList:
        airportlist.append(list[2])
    print(airportlist)
    return airportlist


# 将十个机场随机存入from，to
def randAirportFromTo(airportlist):
    fromlist = random.sample(airportlist, 5)
    tolist = []
    fromToList = []

    for list in airportlist:
        if list not in fromlist:
            tolist.append(list)
    for i in range(5):
        fromToDict = {}
        fromToDict["from"] = fromlist[i]
        fromToDict["to"] = tolist[i]
        fromToList.append(fromToDict)

    # print(fromlist)
    # print(tolist)
    # print(airportlist)
    # print(fromToList)
    return fromToList


# 随机生成任务，与用户信息绑定，入参userid，fromtolist
def randUserTask(userid, fromTolist):
    # 随机获取5个任务，存入list
    getTasksql = "select task_type_id from task_type_flight_game order by rand() limit 5"
    taskResult = function.getResultList(getTasksql)
    taskList = []
    if taskResult != None:
        for result in taskResult:
            taskList.append(result[0])
    # 随机获取5个天气，存入list
    getWeathersql = "select weather_id from weather_flight_game order by rand() limit 5"
    weatherResult = function.getResultList(getWeathersql)
    weatherList = []
    if weatherResult != None:
        for result in weatherResult:
            weatherList.append(result[0])
    #     根据随机出来的task，查出他的油耗和金钱比例，进行计算 需要思考是通过for循环来实现一条一条查询，还是通过sql直接把结果都查出来
    for i in range(5):
        str1=f"{fromTolist[i]['from']}"
        str2=f"{fromTolist[i]['to']}"
        fromList=str1.replace('\'','\\\'')
        toList=str2.replace('\'','\\\'')
        tasksql=f"insert into task_flight_game(user_id, task_type_id, weather_id, addr_from, addr_to, is_done) values ({userid},{taskList[i]},{weatherList[i]},'{fromList}','{toList}',0)"
        function.oprateData(tasksql)


    initUserAirplane(userid)



# 查询出用户国家的所有未关闭的机场，并打乱顺序，将所有信息插入list，并返回该list
def checkCountryList(countryName):
    sql = " select airport_id,airport_ident,airport_name,airport_type,lat_deg,lon_deg,country_name,iso_country,fuel_price from airport_flight_game where country_name= '" + countryName + " ' and airport_type != 'closed' order by rand() "
    result = function.getResultList(sql)
    countryList = []

    # dict={}
    if result != None:
        for row in result:
            countryList.append(row)
    return countryList


# 将用户飞机初始化
def initUserAirplane(userid):
    sql=f"insert into user_airplane_flight_game(userid,airplane_type_id, current_fuel_capacity) values ({userid},1,'1000000')"
    function.oprateData(sql)


# 新用户注册生成任务后，将第一个任务的fromcity当做初始地址赋予到user_flight_game中的current_location中
def initCurrentLocation(userid):
#     查询用户第一个from城市
    firstCityLocation=f"select addr_from from task_flight_game where user_id='{userid}' order by task_id limit 1"
    firstCityLocationResult=function.getResultList(firstCityLocation)
    bornCity=firstCityLocationResult[0][0]
    initBornCity=f"update  user_flight_game current_location = '{bornCity}' where userid = {userid}  "

# # print("-----------------------")
# # for i in list:
# #     print(i)
# register()
# countryList=checkCountryList("United States")
# airportlist=get10AirportsFromCountryList(countryList)
# fromToList=randAirportFromTo(airportlist)
# randUserTask(24,fromToList)

initCurrentLocation(24)

