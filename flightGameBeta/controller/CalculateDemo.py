import flightGameBeta.service.ForPlayService as fp

# calculate result taskId 3
# 计算天气加成
# taskId获取任务数据
# 任务里出发机场经纬度
# 任务里到达机场经纬度
# 通过两个机场经纬度获取距离
# 通过任务类型id去找到任务类型表拿到公里油耗和公里金钱
# 通过距离数计算任务基本油耗和金钱
# 通过天气id获取天气加成油耗和金币
# 基本油耗金币与天气油耗金币计算出最后油耗金币
# 向task表写入当前任务的油耗,金钱
# 向用户详情表写入current_amount ,current_location
# Calculate weather bonus
# taskId gets task data
# Longitude and latitude of the departure airport in the task
# Arrive at the airport latitude and longitude in the task
# Get the distance by latitude and longitude of two airports
# Use the task type id to find the task type table and get the kilometer fuel consumption and kilometer money.
# Calculate the basic fuel consumption and money of the task based on the distance number
# Get weather bonus fuel consumption and gold coins through weather id
# Basic fuel consumption gold coins and weather fuel consumption gold coins are used to calculate the final fuel consumption gold coins
# Write the fuel consumption and money of the current task to the task table
# Write current_amount, current_location to the user details table
Id = 54
fp.settlement(Id)