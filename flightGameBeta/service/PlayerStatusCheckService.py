import flightGameBeta.public_function.DatabaseConnection as fun

#---------------------------------------------------------------------
#Task_flight_game��Ĳ�ѯ,��ѯ�������
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
        
#��������[(User_id, Task_id, Addr_from, Addr_to, Is_done)]
#������ʾ��[(1,1,00A,00B,true),(2,2,00C,00D,false)]
        

#----------------------------------------------------------------------
#��ѯUser_flight_game����ѯ���״̬
def checkPlayerStatus(User_id):
    sql = "select userName, current_location, current_amount from User_flight_game where User_id = '" + User_id + "';"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check player status ERROR!")
        
#��������[(userName, current_location, current_amount)]
#������ʾ��[(ZhuRunzhou,00A,2000)]
        
#------------------------------------------------------------------------
#��ѯUser_airplane_flight_game����ѯ��ҷɻ�״̬
def checkAirplaneStatus(User_id):
    sql = "select current_fuel_capacity from User_airplane_flight_game where User_id = '" + User_id + "';"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check Airplane status ERROR!")
        
#��������[current_fuel_capacity]


#-------------------------------------------------------------------------
#��ӡ���״̬
def printPlayerStatus(User_id):
    result = checkPlayerStatus(User_id)
    print(f"Hello, {result[0]}. You are at {result[1]}. You have {result[2]} money in your poket.")
    return
    

#--------------------------------------------------------------------------
#��ӡ�ɻ�״̬
def printPlaneStatus(User_id):
    result = checkAirplaneStatus(User_id)
    print(f"Hello, you have {result[0]}L fuel in your tank.")
    return



#---------------------------------------------------------------------------
#��ӡ����״̬

