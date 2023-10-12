import time
import flightGameBeta.service.ForPlayService as ForPlayService
import flightGameBeta.service.LogInService as LogInService
import flightGameBeta.service.PlayerStatusCheckService as PlayerStatusCheckService
import flightGameBeta.service.RegitsterService as RegitsterService
import  flightGameBeta.public_function.DatabaseConnection

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

#游戏进行时
def fly(user):
    if (user[5] is not None):
        # 根据userID查询玩家未完成的任务
        # tasks = PlayerStatusCheckService.checkTaskStatus(user[0],0);
        tasks = PlayerStatusCheckService.checkTaskStatus(11, 0);
        print(tasks[0])
        print(f"new task {tasks[0][5]}: ", tasks[0][2], "to", tasks[0][3])
        # 选择目标机场 给出目标机场
        # 询问是否起飞, 1起飞 2等待
        # 选1判断油量是否足够,足够,结算
        # 不够,询问是否加油 1加油 2不加
        # 选1加油,扣钱加油,起飞结算
        # 选2不加,询问是否仍然起飞,1起飞 2等待
        # 选1 坠毁 (循环回登陆成功)
    else:
        print();
        # 生成任务
        # fly()


#login 1
slidePrint("✈✈✈✈✈✈✈✈✈✈✈✈✈welcome to Emergency transportation✈✈✈✈✈✈✈✈✈✈✈✈✈")
choice = input("1. log in                   2. register\nplease input your choice:");
userDetail = login(choice, None,None);
slidePrint("✈✈✈✈✈✈✈✈✈login success✈✈✈✈✈✈✈✈✈")
















# 判断是不是新用户
# user = userDetail[0];
# user = [1, 2, 3, 4, 5, 6];


# print(userDetail)

#随机方法




