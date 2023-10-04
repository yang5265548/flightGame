import random
from geopy import distance

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='some_database_name',
    user='some_user_name',
    password='some_password',
    autocommit=True
)

#functions
#这一部分负责各种函数和方法

#
def checkIfUserIdAlreadyExists(userId):
    sql = "select userid from User_airplane_flight_game;"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
    if userId in result:
        a = True
    else:
        a = False
    return a

#






#####################################################
#game loop
while True:
    #游戏开始
    print("（游戏开始文字）")
    
    #注册/登录
    userId = input("Please enter your user id: ")
    
    #>>>function>>>checkIfUserIdAlreadyExists(userId)
    #方法，判断userid是否在数据库中。参数为userid，方法内部判断userid是否在数据库中，
    #返回一个布尔值,以判断是否创建新账号。
    #True表示账号已经存在，false表示账号不存在，程序将询问玩家是否创建新账号
    
    if checkIfUserIdAlreadyExists(userId) == False:
        
        #玩家没有账号，生成数据并存储进数据库
        startPoint = input("Please select your start point: ")
        #>>>createUserId(userId,startPoint)
        #创建玩家账号，并初始化玩家状态，即随机好机场地图，玩家出生地，任务等。
    
        

    #----------------------------------------
    #玩家已有账号，直接从数据库调取数据（尽量把游戏过程中要用到的参数都汇总写在这个地方吧。。。(＞﹏＜)）

    #>>>checkPlayerStatus(userId)
    #从User_flight_game表中查询并返回玩家状态，返回一个列表，分别表示[userName,current_location,current_amount]
    #比如[zhurunzhou,00A,5000]
    userName = checkPlayerStatus(userId)[0]
    current_location = checkPlayerStatus(userId)[1]
    current_amount = checkPlayerStatus(userId)[2]
        
    #>>>checkAirplaneStatus(userId)
    #从User_airplane_flight_game表和airplane_type_flight_game表中查询并返回一个列表，
    #分别表示现有油量（current_fuel_capacity）和邮箱容量（Fuel_tank_capacity）
    #比如[100,600]
    current_fuel_capacity = checkAirplaneStatus(userId)[0]
    fuel_tank_capacity = checkAirplaneStatus(userId)[1]
    
    #>>>checkAirportStatus(userId)
    #将机场信息从数据库中取出来，包括机场代号，名称，油价等（相当于游戏的地图）
        
    #>>>checkTaskStatus(userId)
    #从Task_flight_game表中查询并返回未完成的任务，返回一个字典，
    #分别表示{Task_id，[出发地（Addr_from ），到达地（Addr_to），任务油耗（Task_oil ），任务奖励（Task_bonus ）]}
        

        

    #-----------------------------------------------------------
    #游戏开始
    while True:
        #先打印出玩家的各种状态，玩家所在地，钱，等
        print(f"Hello, {userName}.")
        print(f"You are at {current_location} now.")
        print(f"You have {current_amount} money in your poket.")

        #玩家可以进行的操作部分
        print("Enter 1 to fly to another place,")
        print("Enter 2 to check the status of your plane,")
        print("Enter 3 to check the status of your tasks,")
        print("Enter E to end this game.")
        a = input("Please select your choise: ")
        
        if a == '1':
            ICAO = input("Please enter your destination: ")
            
            #随机天气影响
            weatherCondition()
            
            #油量消耗
            fuelConsume()

            #飞行过程
            airplaneFly(current_location,ICAO)
            #此函数表示飞机飞行过程，函数将改变数据库中：
            #User_flight_game表中current_location；User_airplane_flight_game表中current_fuel_capacity
            #然后还要加入天气影响，油量不够等各种情况，

        elif a == '2':
            airplaneCheck()
            #不带参数的函数，直接打印出飞机的各种状态,还剩多少油等。(我自己懒得写了ᗜ_ᗜ。。。）

            
            a1 = input("Please enter 1 if you want to fill the tank: ")
            #让玩家决定是否加油
            if a1 == '1':
                airplaneRefuel()
                #给飞机加油的函数，可能要把飞机现有油量，油箱容量，玩家现有金钱，油价等作为参数，并且改变数据库中的数据？
                
        elif a == '3':
            taskCheck()
            #打印出任务的各种数据，起点终点，消耗等。
            #这个函数里还要问玩家是否捡起包裹，放下包裹，这样才能完成任务(╥﹏╥)
            #还要检测玩家是否完成了所有任务，如果完成了所有任务则进入自由模式。

        elif a == 'E':
            break
            

    #---------------------------------------------------------------
    #在游戏结束前，将游戏结果（玩家位置，钱数等信息）存入数据库。
    #>>>syncDatabase(userId,current_location,......)

    
    #游戏结束
    print("Game over.")

