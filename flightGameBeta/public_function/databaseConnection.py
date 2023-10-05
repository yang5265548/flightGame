import mysql.connector

def getProperties(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.readlines();
            list = [];
            for i in content:
                list.append(tuple(i.split("=")));
                dataDict = dict(list);
            return dataDict;
        # 在这里处理文件内容
    except FileNotFoundError:
        print("FileNotFoundError")
    except PermissionError:
        print("PermissionError")
    except Exception as e:
        print(f"UnknowError: {str(e)}")
path = '../config/databaseConnection.properties';
properties = getProperties(path);

connection = mysql.connector
connection.connect(
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
    finally:
        cursor.close()
        connection.close()

# demo
# import public_function.databaseConnection as database
# sql = 'insert into zzz (game_id, goal_id) values(3,7)';
# find data
# print(database.getResultList(sql));
# oprate data
# print(database.oprateData(sql));