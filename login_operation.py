# Import the library
import bcrypt
from calendar_event import get_credentials
import traceback

def add_row_uname(connection,mycur,data):
    try:
        get_credentials()
        file = ""
        with open(f'token.json') as f:
            file = f.read()
        mycur.execute("INSERT INTO users (userid, password, height, gender, credential) VALUES (%s, %s, %s, %s, %s)", (data[0], data[1], data[2], data[3], file))
        connection.commit()
        return 1
    except:
        traceback.print_exc()
        return 0
    
def validation(mycur,data):
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
