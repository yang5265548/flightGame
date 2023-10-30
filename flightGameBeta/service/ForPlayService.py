import flightGameBeta.public_function.DatabaseConnection as fun
import random
from geopy import distance
import math
import flightGameBeta.service.PlayerStatusCheckService as rz


# author:zzy

# 结算(用户id,任务id, 天气对象)
def settlement(taskId):
    # 计算天气加成
    # taskId获取任务数据
    # 任务里出发机场经纬度
    taskDetail = getFromToAddr(taskId);
    # print(taskDetail)
    userId = taskDetail[0][0];
    taskTypeId = taskDetail[0][1];
    weatherId = taskDetail[0][2];
    # 通过两个机场经纬度获取距离
    distanceCount = claculateDistance(taskDetail[0][3], taskDetail[0][4]);
    # 通过任务类型id去找到任务类型表拿到公里油耗和公里金钱
    taskTypeDetail = selectTaskType(taskTypeId);
    perBounds = float(taskTypeDetail[0][2]);
    perOil = float(taskTypeDetail[0][3]);
    # 通过距离数计算任务基本油耗和金钱
    basicBounds = distanceCount * perBounds;
    basicOilConsume = distanceCount * perOil;

    # 通过天气id获取天气加成油耗和金币
    weatherDetail = getRandomWeather(weatherId);
    # print(weatherDetail)
    # 基本油耗金币与天气油耗金币计算出最后油耗金币
    OilConsume = basicOilConsume * (1 - float(weatherDetail[0][3]));
    Bounds = basicBounds * (1 + float(weatherDetail[0][4]));
    # 向task表写入当前任务的油耗,金钱
    result = updateTaskCurrentOilAndMoney(OilConsume, Bounds, taskId, userId, weatherId);

    #修改燃油量
    rz.updateUserAirplaneFlightGame(userId, 0, OilConsume, 0)

    # 向用户详情表写入current_amount ,current_location
    if(result is True):
        result = updateUserCurrentAmountAndLocation(userId, Bounds, taskDetail[0][4]);
    return result;

# 计算距离
def claculateDistance(currentPlace, targetPlace):
    # 通过当前所在地和目的地获取距离
    fromAddr = getAirPortNF(currentPlace);
    toAddr = getAirPortNF(targetPlace);
    fromLat = fromAddr[0][0]
    fromLog = fromAddr[0][1]
    toLat = toAddr[0][0]
    toLlog = toAddr[0][1]
    fromAirport = (fromLat, fromLog);
    # 任务里到达机场经纬度
    toAirport = (toLat, toLlog);
    # 通过两个机场经纬度获取距离
    distanceCount = distance.distance(fromAirport, toAirport).kilometers;
    return distanceCount;

#计算油耗
def calculateFule(distance, taskTypeId, weatherId):
    taskTypeDetail = selectTaskType(taskTypeId);
    perOil = float(taskTypeDetail[0][3]);
    # 通过距离数计算任务基本油耗和金钱
    basicOilConsume = distance * perOil;
    # 通过天气id获取天气加成油耗和金币
    weatherDetail = getRandomWeather(weatherId);
    # print(weatherDetail)
    # 基本油耗金币与天气油耗金币计算出最后油耗金币
    OilConsume = basicOilConsume * (1 + float(weatherDetail[0][3]));
    return OilConsume

# 飞机空飞 1.消耗油量, 当前所在地, 目的地()
def flyNoTask(userId, currentPlace, targetPlace):
    # 通过两个机场经纬度获取距离
    distanceCount = claculateDistance(currentPlace, targetPlace);

    # 通过距离数计算油耗
    basicOilConsume = distanceCount * 10;
    # 扣除飞机油量
    result = rz.updateUserAirplaneFlightGame(userId, 0, basicOilConsume, 0)
    #将当前地址改成目的地
    result = updateUserCurrentAmountAndLocation(userId, None, targetPlace);
    return result;

# taskId获取出发机场,到达机场名称
def getFromToAddr(id):
    sql = f"SELECT user_id, task_type_id as taskTypeId, weather_id, addr_from, addr_to FROM `task_flight_game` where id = '{id}'";
    return fun.getResultList(sql);


# 机场名称获取其经纬度
def getAirPortNF(airportName):
    sql = f"select lat_deg, lon_deg, fuel_price from airport_flight_game where airport_name = '{airportName}'";
    return fun.getResultList(sql);


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
def getRandomWeather(weather_id):
    sql = f"select wf.Weather_id, wf.Weather_name, wf.description, wf.oil_consumption_rate,wf.bonus_per_km_rate from Weather_flight_game wf where Weather_id = '{weather_id}'";
    weatherList = fun.getResultList(sql);
    return weatherList;


#  通过任务id去找到任务类型表拿到公里油耗和公里金钱
def selectTaskType(taskTypeId):
    sql = f"select task_id, task_name, bonus_per_km, oil_consumption from task_type_flight_game where task_id = '{taskTypeId}'";
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
    sql = f"update Task_flight_game set Weather_id = '{weather_id}', Is_done = 1, Task_oil = '{oilConsume}', Task_bonus = '{amount}' where id = '{taskId}' "
    result = fun.oprateData(sql);
    return result;


#  向用户详情表写入current_amount ,current_location
#  currentLocation 当前位置
#  TaskAmount 任务金币
def updateUserCurrentAmountAndLocation(userId, TaskAmount, currentLocation):
    result = None;
    if(TaskAmount is not None and currentLocation is not None):
        sql = f"update User_flight_game set current_location = '{currentLocation}' , current_amount =  current_amount + {TaskAmount} where userId = {userId}"
        result = fun.oprateData(sql);
    elif(TaskAmount is None and currentLocation is not None):
        sql = f"update User_flight_game set current_location = '{currentLocation}' where userId = {userId}"
        result = fun.oprateData(sql);
    elif(TaskAmount is None and currentLocation is None):
        sql = f"update User_flight_game set log_time = current_timestamp  where userId = {userId}"
        result = fun.oprateData(sql);
    return result;


def selectFuelTank(airplaneTypeId):
    sql = f"select airplane_type_id, airplane_type, fuel_tank_capacity from airplane_type_flight_game where airplane_type_id = '{airTypeId}'";
    result = fun.getResultList(sql);
    if result is not None:
        return result;
    else:
        return None;

def calculateHowMuchFuel(airTypeId, currentFuel):
    airplanTypes = selectFuelTank(airTypeId);
    # 油箱大小
    oilTank = airplanTypes[0][1];
    return oilTank - currentFuel


# settlement(1);
