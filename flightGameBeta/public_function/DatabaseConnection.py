import mysql.connector
import flightGameBeta.public_function.GetPropertiesHandler as p
import os


path = os.path.join('../config', 'mysql.properties');
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

        cursor.execute(sql)
        connection.commit()
        print("success")
        return True
    except Exception as e:
        connection.rollback()
        print("error:", str(e))
        return False



#------------------------------------------------------------------------------
# example
import flightGameBeta.public_function.DatabaseConnection as fun

# select
# sql = 'select * from airport';
# print(fun.getResultList(sql));

# # operate
# sql = 'insert into zzz (game_id, goal_id) values(3,7)';
# # oprate data
# print(fun.oprateData(sql));


