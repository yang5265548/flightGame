import flightGameBeta.public_function.DatabaseConnection as fun
import random
from geopy import distance
import math
import flightGameBeta.service.PlayerStatusCheckService as rz


# author:zzy

# Settlement (user id, task id, weather object)
def settlement(taskId):
    # Calculate weather bonus
    # taskId gets task data
    # Longitude and latitude of the departure airport in the task
    taskDetail = getFromToAddr(taskId);
    # print(taskDetail)
    userId = taskDetail[0][0];
    taskTypeId = taskDetail[0][1];
    weatherId = taskDetail[0][2];
    # Get distance from two airports by latitude and longitude
    distanceCount = claculateDistance(taskDetail[0][3], taskDetail[0][4]);
    # Use the task type id to find the task type table and get the mileage fuel consumption and mileage money.
    taskTypeDetail = selectTaskType(taskTypeId);
    perBounds = float(taskTypeDetail[0][2]);
    perOil = float(taskTypeDetail[0][3]);
    # Calculate mission basic fuel consumption and money based on distance
    basicBounds = distanceCount * perBounds;
    basicOilConsume = distanceCount * perOil;

    # Get weather bonus fuel consumption and gold coins through weather ID
    weatherDetail = getRandomWeather(weatherId);
    # print(weatherDetail)
    # Basic fuel consumption gold coins and weather fuel consumption gold coins are used to calculate the final fuel consumption gold coins
    OilConsume = basicOilConsume * (1 - float(weatherDetail[0][3]));
    Bounds = basicBounds * (1 + float(weatherDetail[0][4]));
    # Write the fuel consumption and money of the current task to the task table
    result = updateTaskCurrentOilAndMoney(OilConsume, Bounds, taskId, userId, weatherId);

    #Modify fuel quantity
    rz.updateUserAirplaneFlightGame(userId, 0, OilConsume, 1)

    # Write current_amount, current_location to the user details table
    if(result is True):
        result = updateUserCurrentAmountAndLocation(userId, Bounds, taskDetail[0][4]);
    return result;

# Calculate distance
def claculateDistance(currentPlace, targetPlace):
    # Get distance from current location and destination
    fromAddr = getAirPortNF(currentPlace);
    toAddr = getAirPortNF(targetPlace);
    fromLat = fromAddr[0][0]
    fromLog = fromAddr[0][1]
    toLat = toAddr[0][0]
    toLlog = toAddr[0][1]
    fromAirport = (fromLat, fromLog);
    # Arrival airport latitude and longitude in mission
    toAirport = (toLat, toLlog);
    # Get distance from two airports by latitude and longitude
    distanceCount = distance.distance(fromAirport, toAirport).kilometers;
    return distanceCount;

#Calculate fuel consumption
def calculateFule(distance, taskTypeId, weatherId):
    taskTypeDetail = selectTaskType(taskTypeId);
    perOil = float(taskTypeDetail[0][3]);
    # Calculate mission basic fuel consumption and money based on distance
    basicOilConsume = distance * perOil;
    # Get weather bonus fuel consumption and gold coins through weather ID
    weatherDetail = getRandomWeather(weatherId);
    # print(weatherDetail)
    # Basic fuel consumption gold coins and weather fuel consumption gold coins are used to calculate the final fuel consumption gold coins.
    OilConsume = basicOilConsume * (1 + float(weatherDetail[0][3]));
    return OilConsume

# The plane is empty 1. Fuel consumption, current location, destination ()
def flyNoTask(userId, currentPlace, targetPlace):
    # Get distance from two airports by latitude and longitude
    distanceCount = claculateDistance(currentPlace, targetPlace);

    # Calculate fuel consumption based on distance
    basicOilConsume = distanceCount * 10;
    # Deduct aircraft fuel
    result = rz.updateUserAirplaneFlightGame(userId, 0, basicOilConsume, 1)
    #Change current address to destination
    result = updateUserCurrentAmountAndLocation(userId, None, targetPlace);
    return result;

# taskId gets the departure airport and arrival airport name
def getFromToAddr(id):
    sql = f"SELECT user_id, task_type_id as taskTypeId, weather_id, addr_from, addr_to FROM `task_flight_game` where task_id = '{id}'";
    return fun.getResultList(sql);


# Airport name to get its latitude and longitude
def getAirPortNF(airportName):
    airportName = airportName.replace('\'', '\\\'')
    sql = f"select lat_deg, lon_deg, fuel_price from airport_flight_game where airport_name = '{airportName}'";
    return fun.getResultList(sql);


# Query the list of airports opened by the user (user ID)
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


# Random weather bonus list (randomly generate a weather ID for the task)
def getRandomWeather(weather_id):
    sql = f"select wf.Weather_id, wf.Weather_name, wf.description, wf.oil_consumption_rate,wf.bonus_per_km_rate from Weather_flight_game wf where Weather_id = '{weather_id}'";
    weatherList = fun.getResultList(sql);
    return weatherList;


#  Use the task ID to find the task type table and get the mileage fuel consumption and mileage money.
def selectTaskType(taskTypeId):
    sql = f"select task_type_id, task_name, bonus_per_km, oil_consumption from task_type_flight_game where task_type_id = '{taskTypeId}'";
    result = fun.getResultList(sql);
    if result is not None:
        return result;
    else:
        return None;


#  Query the weather table and obtain weather bonus fuel consumption and gold coins through weather ID
def selectWeather(weather_id):
    sql = f"select Weather_id, Weather_name, description, oil_consumption_rate, bonus_per_km_rate from Weather_flight_game where Weather_id = '{weather_id}'";
    result = fun.getResultList(sql);
    if result is not None:
        return result;
    else:
        return None;


# Write the fuel consumption and money of the current task to the task table
# oilConsume Final fuel consumption
# amount final money
def updateTaskCurrentOilAndMoney(oilConsume, amount, taskId, userId, weather_id):
    sql = f"update Task_flight_game set Weather_id = '{weather_id}', Is_done = 1, Task_oil = '{oilConsume}', Task_bonus = '{amount}' where task_id = '{taskId}' "
    result = fun.oprateData(sql);
    return result;


# Write current_amount, current_location to the user details table
# currentLocation current location
# TaskAmount task gold coins
def updateUserCurrentAmountAndLocation(userId, TaskAmount, currentLocation):
    currentLocation = currentLocation.replace('\'', '\\\'')
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
    sql = f"select airplane_type_id, airplane_type, fuel_tank_capacity from airplane_type_flight_game where airplane_type_id = '{airplaneTypeId}'";
    result = fun.getResultList(sql);
    if result is not None:
        return result;
    else:
        return None;

def calculateHowMuchFuel(airTypeId, currentFuel):
    airplanTypes = selectFuelTank(airTypeId);
    # Fuel tank size
    oilTank = airplanTypes[0][2];
    return oilTank - currentFuel


# settlement(1);
