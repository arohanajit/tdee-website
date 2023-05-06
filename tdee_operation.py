import pymysql

def weight_cal_insert(connection,mycur,uname):
    weight = float(input("Enter weight: "))
    calories = int(input("Enter calories: "))
    mycur.execute("INSERT INTO data (userid, date, weight, calorie) VALUES (%s, NOW(), %s, %s)", (uname, weight, calories,))
    mycur.execute("SELECT * FROM data")
    print(mycur.fetchall())