import pymysql
from datetime import date

def weight_cal_insert(connection,mycur,uname,weight=0,calories=0):
    if weight==0 or calories==0:
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

def tdee(connection,mycur):
    mycur.execute("SELECT userid,height,gender FROM users")
    users = mycur.fetchall()
    users = [i for i in users]

    def tdee_calc(daily_weight,daily_calories,height,gender):
        WEIGHT_DAYS = len(daily_weight)
        BMR_ACTIVITY_FACTOR = {
            "M": 1.5,  # Male BMR activity factor
            "F": 1.4,  # Female BMR activity factor
        }
        # Calculate initial BMR and TDEE
        if gender == "M":
            bmr = 88.36 + (13.4 * height) - (5.7 * sum(daily_weight)) + (8.6 * WEIGHT_DAYS)
        else:
            bmr = 447.6 + (9.2 * height) - (4.3 * sum(daily_weight)) + (3.1 * WEIGHT_DAYS)
        tdee = bmr * BMR_ACTIVITY_FACTOR[gender]

        return round(tdee,2), round(sum(daily_weight)/WEIGHT_DAYS,2), round(sum(daily_calories)/len(daily_calories),2)
    
    for i in users:
        mycur.execute("SELECT weight, calorie FROM data WHERE userid=%s",i[0])
        c = mycur.fetchall()
        weight = [int(j[0]) for j in c]
        calorie = [int(j[1]) for j in c]
        x,y,z = tdee_calc(weight,calorie,int(i[1]),i[2])
        print(f"tdee: {x}  Average Weight: {y} Average Calorie: {z}")
    
    

