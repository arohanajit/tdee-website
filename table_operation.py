# Import the library
import pymysql
import bcrypt


def connection_estb():
    # Define the connection parameters
    host = "sql12.freesqldatabase.com"
    port = 3306 # or your custom port
    user = "sql12616283"
    password = "peM429qpNa"
    database = "sql12616283"

    # Create a connection object
    connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
    mycur = connection.cursor()

    return connection, mycur

def add_row_uname(connection,mycur,data):
    try:
        mycur.execute("INSERT INTO users (userid, password) VALUES (%s, %s)", (data[0], data[1]))
        connection.commit()
        return
    except Exception as e:
        print(e)
        return
    
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
        return False
