import flightGameBeta.public_function.DatabaseConnection as fun

#---------------------------------------------------------------------
#Task_flight_game表的查询,查询任务情况
def checkTaskStatus(User_id,Task_id,Is_done):
    if User_id  is not None:
        sql1 = " and User_id = " + User_id 
    else:
        sql1 = None
        
    if Task_id is not None:
        sql2 = " and Task_id = " + Task_id
    else:
        sql2 = None
        
    if Is_done is not None:
        sql3 = " and Is_done = " + Is_done
    else:
        sql3 = None
    
    if User_id  is not None or Task_id is not None or Is_done is not None:
        sql = "select User_id, Task_id, Addr_from, Addr_to, Is_done from Task_flight_game where User_id like '%'" + sql1 + sql2 + sql3 +"';"
        result = fun.getResultList(sql)
        if result is not None:
            return result
        else:
            print("Check task status ERROR!")
    else:
        print("Check task status ERROR!")
        
#输出结果：[(User_id, Task_id, Addr_from, Addr_to, Is_done)]
#输出结果示例[(1,1,00A,00B,true),(2,2,00C,00D,false)]
        

#----------------------------------------------------------------------
#查询User_flight_game表，查询玩家状态
def checkPlayerStatus(User_id):
    sql = "select userName, current_location, current_amount from User_flight_game where User_id = '" + User_id + "';"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check player status ERROR!")
        
#输出结果：[(userName, current_location, current_amount)]
#输出结果示例[(ZhuRunzhou,00A,2000)]
        
#------------------------------------------------------------------------
#查询User_airplane_flight_game表，查询玩家飞机状态
def checkAirplaneStatus(User_id):
    sql = "select current_fuel_capacity from User_airplane_flight_game where User_id = '" + User_id + "';"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check Airplane status ERROR!")
        
#输出结果：[current_fuel_capacity]


#-------------------------------------------------------------------------
#打印玩家状态
def printPlayerStatus(User_id):
    result = checkPlayerStatus(User_id)
    print(f"Hello, {result[0]}. You are at {result[1]}. You have {result[2]} money in your poket.")
    return
    

#--------------------------------------------------------------------------
#打印飞机状态
def printPlaneStatus(User_id):
    result = checkAirplaneStatus(User_id)
    print(f"Hello, you have {result[0]}L fuel in your tank.")
    return



#---------------------------------------------------------------------------
#打印任务状态

