# 游戏入口方法
# from flightGameBeta.controller.LoginAndRegisterDemo import slidePrint
import LoginAndRegisterDemo as o
from flightGameBeta.service.ForPlayService import flyNoTask, claculateDistance, calculateFule, settlement, getAirPortNF, \
    calculateHowMuchFuel, selectFuelTank
from flightGameBeta.service.LogInService import user_exist, user_exist_mi
from flightGameBeta.service.PlayerStatusCheckService import checkTaskStatus, checkPlayerStatus, checkAirplaneStatus
import flightGameBeta.service.PlayerStatusCheckService as rz
from flightGameBeta.service.RegitsterService import initUserAirplane
from guess import guess_reddle


def play():
    global ans
    while True:
        ans = input("do you want to fly?:Y/N..")
        if ans != "Y" and ans != "y":
            print("You need to Wait~~~~~~untill you want to fly")
            print("~~~~~~~")
            print("~~~~~~~")
            print("~~~~~~~")
            continue
        else:
            planeStu = rz.checkAir(userid)
            currentfuel = planeStu[0][0]
            airplaneTypeId = planeStu[0][1]

            distance = claculateDistance(addrfrom, addrto)
            fuleAll = calculateFule(distance, tasktypeid, weatherid)
            if currentfuel >= fuleAll:
                settlement(taskid)
                break
            else:
                fromAirportFuelPrice = getAirPortNF(addrfrom)
                toAirportFuelPrice = getAirPortNF(addrto)
                ans = input(f"maybe your fule is not enough to finsh the task,"
                            f"the current airport fuel price is {fromAirportFuelPrice[0][2]} ,"
                            f"the next airport fuel price is {toAirportFuelPrice[0][2]} ,"
                            f"do you want to add the fule now : y/n")
                canFuel = calculateHowMuchFuel(airplaneTypeId, currentfuel)

                if ans == "Y" or ans == "y":
                    ueserwanttoaddfuel = float(input(
                        f"please enter the oil quantity(Current amount of money available for refueling: {float(currentamount) / float(fromAirportFuelPrice[0][2])} L): "))
                    rz.updateUserAirplaneFlightGame(userid, 0, ueserwanttoaddfuel, 0)
                    continue
                else:
                    userStatus = checkPlayerStatus(userid)
                    currentAmount = userStatus[0][2]
                    if currentAmount != 0:
                        print("U fuel do not enough, please consume money to complement oil until no money")
                    else:
                        print(
                            "you can't finsh the task ,cause you dont have enough feul~~~~~~so your have crashed~~~~");
                        print("BUT WE HAVE A CHANCE TO U, LETS START!!!")
                        guess_reddle()
                        airplanTypes = selectFuelTank(airplaneTypeId)
                        # 油箱大小
                        # Fuel tank size
                        oilTank = airplanTypes[0][1]
                        # 重置用户飞机油量至满油
                        # Reset the user's aircraft fuel level to full
                        rz.updateUserAirplaneFlightGame(userid, airplaneTypeId, oilTank, 2)
                        continue


userDetail = o.loginAndRegister()
# userDetail的数据样例 tuple [(19, 'yangyang', '7c4a8d09ca3762af61e59520943dc26494f8941b', None, 0, None)]
username = userDetail[0][1]
password = userDetail[0][2]
userid = userDetail[0][0]
currentamount = userDetail[0][4]
print(userid)
print(username)
# 判断时候是新用户，新用户直接开始执行程序，老用户去读取任务进度
# Determine whether it is a new user. The new user starts executing the program directly, and the old user reads the task progress.

result = user_exist_mi(username, password)
while True:
    if result is not None:
        # 说明不是新用户，需要调取历史任务
        # It means you are not a new user and you need to retrieve historical tasks.
        userTaskResult = checkTaskStatus(userid, 0)
        print("The all unfinshed list:")
        if (userTaskResult is None):
            print("conguratulation!, u through all task, please expected next version")
            break
        for num, list in enumerate(userTaskResult):
            # list 样例：(24, 7, 'Fenner Ranch Airport', 'John Harris Field', 0, 'G')
            print(f"{num}: task_name: {list[5]} From: {list[2]} To:{list[3]}")
        usechoose = int(input("select the taskid: "))
        # 拿到的任务id
        # The task id obtained
        taskid = userTaskResult[usechoose][6]
        # 拿到的任务初始地
        # The initial location of the task obtained
        addrfrom = userTaskResult[usechoose][2]
        # 拿到的任务结束地
        # The end point of the obtained mission
        addrto = userTaskResult[usechoose][3]
        # 拿到天气id
        # Get weather id
        weatherid = userTaskResult[usechoose][7]
        # 拿到tasktypeid
        # get tasktypeid
        tasktypeid = userTaskResult[usechoose][1]
        #     判断当前所在地是否是任务初始地
        # Determine whether the current location is the initial location of the task
        playerStatusList = checkPlayerStatus(userid)
        currentLoction = playerStatusList[0][1]
        if addrfrom != currentLoction:
            while True:
                ans = input("you need to fly to the task start place:Y/N ")
                if ans == "Y" or ans == "y":
                    flyNoTask(userid, currentLoction, addrfrom)
                    break
                else:
                    continue
            play()
        # 调用是的逻辑

        else:
            play()
