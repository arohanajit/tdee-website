# Import the library
import pymysql


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

def add_row_uname(connection,mycur):
    try:
        test_values = '''insert into users values ('testuname','testpwd')'''
        mycur.execute(test_values)
        connection.commit()
        return
    except Exception as e:
        print(e)
        return
