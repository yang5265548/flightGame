def zz():
    return 1;

import public_function.databaseConnection as c

c.getSqlResult()
import random

# 定义一组数字
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 指定要随机选择的数字数量
num_to_select = 3

# 使用random.sample函数从列表中随机选择指定数量的数字
for i in range(20):
    random_numbers = random.sample(numbers, num_to_select)
    print(random_numbers)

# 打印随机选择的数字
# print(random_numbers)
