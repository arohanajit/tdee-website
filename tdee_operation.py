from datetime import date

def weight_cal_insert(connection, cursor, uname, weight=0, calories=0):
    if weight == 0 or calories == 0:
        weight = input("Enter weight: ")
        calories = input("Enter calories: ")
    cursor.execute("INSERT INTO data (userid, date, weight, calorie) VALUES (%s, CURDATE(), %s, %s)", (uname, weight, calories))
    connection.commit()
    cursor.execute("SELECT * FROM data")
    print(cursor.fetchall())

def no_entry(connection, cursor):
    now = date.today()
    cursor.execute("SELECT userid, MAX(date) as latest_date FROM data GROUP BY userid")
    ids = cursor.fetchall()
    for i in ids:
        if now != i[1]:
            cursor.execute("SELECT weight, calorie FROM data WHERE userid=%s ORDER BY date DESC LIMIT 1", (i[0],))
            vals = cursor.fetchone()
            cursor.execute("INSERT INTO data(userid, date, weight, calorie) VALUES (%s, %s, %s, %s)", (i[0], now, vals[0], vals[1]))
            connection.commit()
            print(f"Data copied for previous date for {i[0]}")

def tdee(connection, cursor, uname):
    def tdee_calc(daily_weight, daily_calories, height, gender):
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

        return round(tdee, 2), round(sum(daily_weight) / WEIGHT_DAYS, 2), round(sum(daily_calories) / len(daily_calories), 2)

    cursor.execute("SELECT height, gender FROM users WHERE userid=%s", (uname,))
    i = cursor.fetchone()
    cursor.execute("SELECT weight, calorie FROM data WHERE userid=%s", (uname,))
    c = cursor.fetchall()
    weight = [float(j[0]) for j in c]  # Changed to float
    calorie = [int(j[1]) for j in c]
    return tdee_calc(weight, calorie, float(i[0]), i[1])  # Changed to float