import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='metropolia',
        user='root',
        password='123456',
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

def oprateData(insert_sql):
    cursor = connection.cursor();
    try:
        # 执行插入操作
        cursor.execute(insert_sql)

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