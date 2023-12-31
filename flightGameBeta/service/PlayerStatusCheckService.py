import random
import flightGameBeta.public_function.DatabaseConnection as fun


# updateUserAirplaneFlightGame
# if addOrMinus == 0  add oil
# if addOrMinus == 1  minus oil
# if addOrMinus == 2  reset oil
def updateUserAirplaneFlightGame(userid, airplane_type_id, fuel, addOrMinus):
    if(addOrMinus == 0):
        sql = f"update user_airplane_flight_game set current_fuel_capacity = current_fuel_capacity + {fuel} where userid = {userid} and airplane_type_id = {airplane_type_id};"
    elif(addOrMinus == 1):
        sql = f"update user_airplane_flight_game set current_fuel_capacity = current_fuel_capacity - {fuel} where userid = {userid} and airplane_type_id = {airplane_type_id};"
    elif (addOrMinus == 2):
        sql = f"update user_airplane_flight_game set current_fuel_capacity = {fuel} where userid = {userid} and airplane_type_id = {airplane_type_id};"
    fun.getResultList(sql)

# initialization of player status
def initialPlayerStatus(user_id):
    sql1 = f"select Addr_from from task_flight_game where user_id = {user_id};"
    sql2 = f"select Addr_to from task_flight_game where user_id = {user_id};"
    lst1 = fun.getResultList(sql1)
    lst2 = fun.getResultList(sql2)
    lst = lst1 + lst2
    current_location = lst[random.randint(0, 9)]
    sql3 = (f"update user_flight_game set current_location = '{current_location[0]}' where userid = {user_id};"
            f"update user_flight_game set current_amount = 100000 where userid = {user_id};")
    fun.getResultList(sql3)


# initialization of airplane status
def initialPlaneStatus(user_id):
    sql = f"insert into user_airplane_flight_game (userid, airplane_type_id, current_fuel_capacity) values ({user_id}, 1, 10000);"
    fun.getResultList(sql)


# ---------------------------------------------------------------------
# Use task_flight_game, check tasks
def checkTaskStatus(user_id, is_done):
    sql = (f"select f.User_id, f.task_type_id, f.Addr_from, f.Addr_to, f.Is_done, t.task_name,f.task_id,f.weather_id "
           f"from Task_flight_game f left join task_type_flight_game t on t.task_type_id = f.task_type_id "
           f"where user_id= {user_id} and is_done = {is_done}")
    result = fun.getResultList(sql)
    return result


# Output example: [(User_id, Task_id, Addr_from, Addr_to, Is_done)]
# Output example: [(1,1,00A,00B,true),(2,2,00C,00D,false)]


# ----------------------------------------------------------------------
# Use user_flight_game check player location and money
def checkPlayerStatus(User_id):
    sql = f"select username, current_location, current_amount from user_flight_game where userid = {User_id};"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check player status ERROR!")



# Output example: [(userName, current_location, current_amount)]
# Output example: [(ZhuRunzhou,00A,2000)]

# ------------------------------------------------------------------------
# Use user_airplane_flight_game check player's plane fuel condition
def checkAirplaneStatus(User_id):
    sql = f"select current_fuel_capacity from user_airplane_flight_game where userid = {User_id}"
    result = fun.getResultList(sql)
    if result is not None:
        return result[0]
    else:
        print("Check Airplane status ERROR!")


def checkAir(User_id):
    sql = f"select current_fuel_capacity, airplane_type_id from user_airplane_flight_game where userid = {User_id}"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check Airplane status ERROR!")



# Output example: [current_fuel_capacity]


# -------------------------------------------------------------------------
# print player location and moeny
def printPlayerStatus(User_id):
    result = checkPlayerStatus(User_id)
    print(f"Hello, {result[0][0]}. You are at {result[0][1]}. You have {result[0][2]} money in your poket.")
    print("\n\n")
    return


# --------------------------------------------------------------------------
# player plane fuel amount
def printPlaneStatus(User_id):
    result = checkAirplaneStatus(User_id)
    print(f"Hello, you have {result[0]}L fuel in your tank.")
    print("\n\n")
    return


# ---------------------------------------------------------------------------
# print tasks
def printTaskStatus(User_id):
    result = checkTaskStatus(User_id, 0)
    # [(10, 6, 'John Reid Airport', 'Unity Health Specialty Care Heliport', 0, 'F'),
    # (10, 2, 'Airbatco Field', 'Western Spur Airport', 0, 'B'),
    # (10, 7, 'Baranof Warm Springs Float and Seaplane ', 'Ransome Heliport', 0, 'G'),
    # (10, 5, 'Hill Airport', 'Delta Daves Airport', 0, 'E')]
    for i in result:
        print(f"Flying from {i[2]} to {i[3]}")

    print("\n\n")


# ------------------------------------------------------------------------------
# Find ICAO from name
def findICAO(name):
    sql = f"select airport_ident from airport_flight_game where airport_name = '{name}';"
    result = fun.getResultList(sql)
    return result[0][0]


# Find name from ICAO
def findName(ICAO):
    sql = f"select airport_name from airport_flight_game where airport_ident = '{ICAO}';"
    result = fun.getResultList(sql)
    return result[0][0]


# ---------------------------------------------------------------------------------
# Check status function
def checkStatus(uerId):
    while True:
        print("Input 1 to check player status.")
        print("Input 2 to check plane status.")
        print("Input 3 to check tasks status.")
        print("Input something else to leave.")
        i = input("Enter your choice: ")
        if i == '1':
            printPlayerStatus(uerId)
        elif i == '2':
            printPlaneStatus(uerId)
        elif i == '3':
            printTaskStatus(uerId)
        else:
            break


# updateUserAirplaneFlightGame("1",0,1,1)

