import flightGameBeta.public_function.DatabaseConnection as function
import flightGameBeta.public_function.passwordtool as ps


def user_exist(username, password):
    shaPass = ps.sha1password(password)
    sql = f"select * from user_flight_game where username='{username}' and password='{shaPass}'";
    result = function.getResultList(sql)
    return result;





