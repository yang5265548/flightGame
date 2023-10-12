import flightGameBeta.service.RegitsterService as r

#随机任务  随机天气加成 2
#查出输入国家的的所有未关闭机场供用户选择
# Find all unclosed airports in the input country for users to choose from
list = r.checkCountryList("United States")
# 从机场列表中随机选出十个机场
# Ten airports are randomly selected from the airport list
tenairportslist = r.get10AirportsFromCountryList(list)
# 将十个机场进行分组，随机组成5个出发，到达组合，
# Group ten airports and randomly form 5 tasks
fromtolist = r.randAirportFromTo(tenairportslist)
# 随机给用户生成5个任务，随机给任务分配天气类型
# Randomly generate 5 tasks for the user, and randomly assign weather types to the tasks
userId = 18
r.randUserTask(userId, fromtolist)