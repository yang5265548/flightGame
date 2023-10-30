# 游戏入口方法
# from flightGameBeta.controller.LoginAndRegisterDemo import slidePrint
import LoginAndRegisterDemo as o
from flightGameBeta.service.LogInService import user_exist, user_exist_mi
from flightGameBeta.service.PlayerStatusCheckService import checkTaskStatus

# print("Welcome to YM2Z Global Relief~~~~")
# o.slidePrint("✈✈✈✈✈✈✈✈✈✈✈✈✈Welcome to YM2Z Global Relief~~~~✈✈✈✈✈✈✈✈✈✈✈✈✈")

# 登录，让用户输入用户名，判断是否有用户，没有的话调用注册接口
# choice = input("1. log in                   2. register\nplease input your choice:");
# userDetail = o.login(choice, None,None);
userDetail = o.login(1, 'yangyang','123456');
# o.slidePrint("✈✈✈✈✈✈✈✈✈login success✈✈✈✈✈✈✈✈✈")
# userDetail的数据样例 tuple [(19, 'yangyang', '7c4a8d09ca3762af61e59520943dc26494f8941b', None, 0, None)]
username=userDetail[0][1]
password=userDetail[0][2]
userid=userDetail[0][0]
print(userid)
print(username)
# 判断时候是新用户，新用户直接开始执行程序，老用户去读取任务进度
result=user_exist_mi(username,password)
if result is not None:
    # 说明不是新用户，需要调取历史任务
    userTaskResult=checkTaskStatus(userid,0)
    print("The all unfinshed list:")
    for num,list in enumerate(userTaskResult):
        # list 样例：(24, 7, 'Fenner Ranch Airport', 'John Harris Field', 0, 'G')
        print(f"{num}: task_name: {list[5]} From: {list[2]} To:{list[3]}")
    print("Let begin the first unfinsh task")