import mysql.connector
import flightGameBeta.public_function.GetPropertiesHandler as p
import os

# 必须要用os拼路径, 否则路径会找不到2
path = os.path.join('config','Mysql.properties');
properties = p.getProperties(path);
connection = mysql.connector.connect(
    host=properties.get('host'),
    port=properties.get('port'),
    database=properties.get('database'),
    user=properties.get('user'),
    password=properties.get('password'),
    autocommit=True
);


def getResultList(sql):
    cursor = connection.cursor();
    cursor.execute(sql);
    result = cursor.fetchall();
    if cursor.rowcount > 0:
        return result;
    else:
        return None;


def oprateData(sql):
    cursor = connection.cursor();
    try:
        # 执行插入操作
        cursor.execute(sql)
        connection.commit()
        print("数据插入成功")
        return True
    except Exception as e:
        connection.rollback()
        print("数据插入失败:", str(e))
        return False



#------------------------------------------------------------------------------
# example
# import flightGameBeta.public_function.DatabaseConnection as fun

# select
# sql = 'select * from airport';
# print(fun.getResultList(sql));

# operate
# sql = 'insert into zzz (game_id, goal_id) values(3,7)';
# oprate data
# print(fun.oprateData(sql));


