import flightGameBeta.public_function.DatabaseConnection as fun
import random
from geopy import distance
import PlayerStatusCheckService as rz

# author:zzy

# 结算(用户id,任务id, 天气对象)
def settlement(taskId, userId, weatherId):
    #计算天气加成
    #taskId获取任务数据
    # 任务里出发机场经纬度
    taskDetail = rz.checkTaskStatus(taskId);
    fromAirport = (1,2);
    # 任务里到达机场经纬度
    toAirport = (3, 4);
    #通过两个机场经纬度获取距离
    distanceCount = distance.distance('newport_ri', 'cleveland_oh').kilometers
    # 通过任务id去找到任务类型表拿到公里油耗和公里金钱

    #通过距离数计算任务基本油耗和金钱

    # 通过天气id获取天气加成油耗和金币

    # 基本油耗金币与天气油耗金币计算出最后油耗金币

    # 向task表写入当前任务的油耗,金钱

    # 向用户详情表写入current_amount ,current_location


    return

# 查询用户已开启机场列表(用户ID)
def getUserCity(userId):
    sql = (f"select "
           "af.Airport_id,"
           "af.Airport_ident,"
           "af.Airport_name,"
           "af.Airport_ident,"
           "af.Airport_name,"
           "af.Airport_type,"
           "af.Lat_deg,"
           "af.Lon_deg,"
           "af.Country_name,"
           "af.Iso_country,"
           "af.Fuel_price"
           "from User_airport_flight_game uaf"
           "left join Airport_flight_game af on af.airport_id = uaf.airport_id"
           f"where uaf.userId = '{userId}'");
    return fun.getResultList(sql);

# 随机天气加成列表(为任务随机出一个天气id)
def getRandomWeather(Weather_id):
    sql = "select wf.Weather_id, wf.Weather_name, wf.description, wf.oil_consumption_rate,wf.bonus_per_km_rate from Weather_flight_game wf";
    if(Weather_id != '' and Weather_id is not None):
        sql = sql+f" where wf.Weather_id = {Weather_id}";
    weatherList = fun.getResultList(sql);
    return random.choice(weatherList);

#  通过任务id去找到任务类型表拿到公里油耗和公里金钱
def selectTaskType(taskId):
    sql = f"select task_id, task_name, bonus_per_km, oil_consumption from task_type_flight_game where task_id = '{taskId}'";
    result = fun.getResultList(sql);
    if result is not None:
        return result;
    else:
        return None;

#  查询天气表 通过天气id获取天气加成油耗和金币
def selectWeather(weather_id):
    sql = f"select Weather_id, Weather_name, description, oil_consumption_rate, bonus_per_km_rate from Weather_flight_game where Weather_id = '{weather_id}'";
    result = fun.getResultList(sql);
    if result is not None:
        return result;
    else:
        return None;

#  向task表写入当前任务的油耗,金钱
#  oilConsume 最终油耗
#  amount 最终金钱
def updateTaskCurrentOilAndMoney(oilConsume, amount, taskId, userId, weather_id):
    sql = f"update Task_flight_game set Weather_id = '{weather_id}', Is_done = 'true', Task_oil = '{oilConsume}', Task_bonus = '{amount}' where Task_id = '{taskId}' and User_id = '{userId}'"
    result = fun.oprateData(sql);
    return result;

#  向用户详情表写入current_amount ,current_location
#  currentLocation 当前位置
#  TaskAmount 任务金币
def updateUserCurrentAmountAndLocation(userId, TaskAmount, currentLocation):
    sql = f"update User_flight_game set current_location = current_location + {TaskAmount}, current_amount =  {currentLocation} where userId = {userId}"
    result = fun.oprateData(sql);
    return result;



