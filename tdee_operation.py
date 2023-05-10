import pymysql
from datetime import date

def weight_cal_insert(connection,mycur,uname):
    weight = input("Enter weight: ")
    calories = input("Enter calories: ")
    mycur.execute("INSERT INTO data (userid, date, weight, calorie) VALUES (%s, CURDATE(), %s, %s)", (uname, weight, calories,))
    mycur.execute("SELECT * FROM data")
    print(mycur.fetchall())

def no_entry(connection,mycur):
    now = date.today()
    mycur.execute("SELECT userid, MAX(date) as latest_date FROM data GROUP BY userid")
    ids = mycur.fetchall()
    for i in ids:
        if now != i[1]:
            mycur.execute("SELECT weight,calorie FROM data WHERE userid=%s ORDER BY date DESC LIMIT 1",i[0])
            vals = mycur.fetchall()
            mycur.execute("INSERT INTO data(userid, date, weight, calorie) VALUES (%s,%s,%s,%s)",(i[0],now,vals[0][0],vals[0][1]))
            print(f"Data copied for previous date for {i[0]}")
        