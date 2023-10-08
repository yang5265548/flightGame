import flightGameBeta.public_function.DatabaseConnection as fun
import random
from geopy import distance

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
    if(Weather_id != '' and Weather_id != None):
        sql = sql+f" where wf.Weather_id = {Weather_id}";
    weatherList = fun.getResultList(sql);
    return random.choice(weatherList);

# 结算(用户id,飞机油耗量,任务金钱奖励,天气对象)
def settlement(taskId, userId, oilConsume, money, weatherId):
    #计算天气加成
    #taskId获取任务数据
    # 任务里出发机场经纬度
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

    # 向用户详情表写入金币.


    # 向用户详情表写入current_amount ,current_location


    return



#  查询任务类型表
def selectTaskType(userId):
    sql = "select Task_id, Addr_from, Addr_to from Task_flight_game where User_id = '" + userId +"'"
    result = fun.getResultList(sql)
    if result is not None:
        return result
    else:
        print("Check task status ERROR!")
#  查询天气表
#  计算油耗(+随即天气油耗)