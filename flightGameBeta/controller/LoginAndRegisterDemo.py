import time
import flightGameBeta.service.ForPlayService as ForPlayService
import flightGameBeta.service.LogInService as LogInService
import flightGameBeta.service.PlayerStatusCheckService as PlayerStatusCheckService
import flightGameBeta.service.RegitsterService as RegitsterService
import flightGameBeta.public_function.DatabaseConnection

def login(choice, username, password):
    if(username is None and password is None):
        while (choice != '1' and choice != '2'):
            print("please input correct order and try again");
            choice = input("1. log in                   2. register\nplease input your choice:");
        if (choice == '1'):
            username = input("please enter your username: ");
            password = input("please enter your password: ");
            result = LogInService.user_exist(username, password);
            result = loginAgain(result);
        elif(choice == '2'):
            uplist = RegitsterService.register();
            result = login(1, uplist[0], uplist[1]);
    else:
            result = LogInService.user_exist(username, password);
            result = loginAgain(result);
    return result;


def loginAgain(result):
    while (result is None):
        print("please check your username and password and try again");
        username = input("please enter your username: ");
        password = input("please enter your password: ");
        result = LogInService.user_exist(username, password);
        if(result is not None):
            return result;
        print("3. back to previous page        other. continue")
        choice = input("please input your choice:");
        if (choice == '3'):
            result = login(choice, None,None);
    return result;

def slidePrint(title):
    for char in title:
        print(char, end="");
        time.sleep(0.01);
    print('\n');
    time.sleep(0.002);


#login 1
def loginAndRegister():
    slidePrint("✈✈✈✈✈✈✈✈✈✈✈✈✈welcome to Emergency transportation✈✈✈✈✈✈✈✈✈✈✈✈✈")
    choice = input("1. log in                   2. register\nplease input your choice:");
    userDetail = login(choice, None,None);
    if(userDetail[0][5] is None):
        countryNameStratWord = input("input countryName startWord");
        countryNames = RegitsterService.checkAllCountryListStartWith(countryNameStratWord);
        for index, i in enumerate(countryNames):
            print(f"{index}. {i}");
        countryNameNumber = int(input("input countryName number: "));
        countryName = countryNames[countryNameNumber]
        tasks = RegitsterService.initTask(countryName, userDetail[0][0]);
        # Get the from of the first array
        airportFirstTask = tasks[0][3];
        ForPlayService.updateUserCurrentAmountAndLocation(userDetail[0][0], None, airportFirstTask);
        ForPlayService.updateUserCurrentAmountAndLocation(userDetail[0][0], None, None);
        RegitsterService.initUserAirplane(userDetail[0][0])
    slidePrint("✈✈✈✈✈✈✈✈✈login success✈✈✈✈✈✈✈✈✈");
    return userDetail;

















# 判断是不是新用户
# user = userDetail[0];
# user = [1, 2, 3, 4, 5, 6];


# print(userDetail)

#随机方法




