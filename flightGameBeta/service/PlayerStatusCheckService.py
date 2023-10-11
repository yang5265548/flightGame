import flightGameBeta.public_function.DatabaseConnection as fun

#---------------------------------------------------------------------
#Task_flight_game��Ĳ�ѯ,��ѯ�������
def checkTaskStatus(user_id,is_done):
    sql = (f"select f.User_id, f.Task_id, f.Addr_from, f.Addr_to, f.Is_done, t.task_name "
           f"from Task_flight_game f left join task_type_flight_game t on t.task_id = f.task_id "
           f"where user_id= {user_id} and is_done = {is_done}")
    result = fun.getResultList(sql)
    return result

        
#��������[(User_id, Task_id, Addr_from, Addr_to, Is_done)]
#������ʾ��[(1,1,00A,00B,true),(2,2,00C,00D,false)]
        

#----------------------------------------------------------------------
#��ѯUser_flight_game����ѯ���״̬
def checkPlayerStatus(User_id):
    sql = "select userName, current_location, current_amount, log_time from User_flight_game where User_id = '" + User_id + "';"
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

