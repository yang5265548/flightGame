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

    sql = "select User_id, Task_id, Addr_from, Addr_to, Is_done from Task_flight_game where User_id like '%'" + sql1 + sql2 + sql3 +"';"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check task status ERROR!")



