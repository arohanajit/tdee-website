import pymysql

def weight_cal_insert(connection,mycur,uname):
    weight = input("Enter weight: ")
    calories = input("Enter calories: ")
    mycur.execute("INSERT INTO data (userid, date, weight, calorie) VALUES (%s, CURDATE(), %s, %s)", (uname, weight, calories,))
    mycur.execute("SELECT * FROM data")
    print(mycur.fetchall())