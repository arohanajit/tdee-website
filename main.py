# Import the library
import pymysql

# Define the connection parameters
host = "database-1.cgfioyjzasue.us-east-2.rds.amazonaws.com"
port = 3306 # or your custom port
user = "admin"
password = "10293847"
database = "sample"

# Create a connection object
connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
mycur = connection.cursor()

create_table_1 = '''
CREATE TABLE users (
  userid VARCHAR(255) PRIMARY KEY,
  password VARCHAR(255)
)'''

mycur.execute(create_table_1)
mycur.fetchall()
