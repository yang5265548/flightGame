import mysql.connector


def excuseSql():
    # database
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='metropolia',
        user='root',
        password='123456',
        autocommit=True
    );


    def getSqlResult(sql):
        cursor = connection.cursor();
        cursor.execute(sql);
        if(cursor.rowcount > 0):
            return cursor.fetchall();
        else:
            return None;


