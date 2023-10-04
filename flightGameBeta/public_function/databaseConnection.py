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


# demo
# import public_function.databaseConnection as c
#
# sql = 'select * from airport';
# print(c.getResultList(sql));