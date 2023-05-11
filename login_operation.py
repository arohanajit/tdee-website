# Import the library
import pymysql
import bcrypt

def add_row_uname(connection,mycur,data):
    try:
        mycur.execute("INSERT INTO users (userid, password, height, gender) VALUES (%s, %s, %s, %s)", (data[0], data[1], data[2], data[3]))
        connection.commit()
        return 1
    except Exception as e:
        print(e)
        return 0
    
def validation(connection,mycur,data):
    try:
        mycur.execute("SELECT * FROM users WHERE userid = %s",(data[0]))
        val = mycur.fetchall()
        if len(val)!=0:
            if bcrypt.checkpw(data[1].encode(),val[0][1].encode()):
                return val[0][0]
        return ''
    except Exception as e:
        print(e)
        return ''
