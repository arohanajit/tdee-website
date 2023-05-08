# Import the library
import pymysql

# Define the connection parameters
host = "sql12.freesqldatabase.com"
port = 3306 # or your custom port
user = "sql12616283"
password = "peM429qpNa"
database = "sql12616283"

# Create a connection object
connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
mycur = connection.cursor()
mycur.execute("SET FOREIGN_KEY_CHECKS = 0")
mycur.execute("TRUNCATE TABLE data")
mycur.execute("TRUNCATE TABLE users")
mycur.execute("SET FOREIGN_KEY_CHECKS = 1")
# mycur.execute("DROP TABLE data")
connection.commit()
connection.close()

