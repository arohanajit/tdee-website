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

# Create username password table
create_table_1 = '''
CREATE TABLE users (
  userid VARCHAR(255) PRIMARY KEY,
  password VARCHAR(255),
  height NUMERIC,
  gender ENUM('M','F')
)'''

mycur.execute(create_table_1)


# create values database linked by foreign key username
create_table_2 = '''
CREATE TABLE data (
    userid VARCHAR(255),
    date DATE,
    weight NUMERIC,
    calorie NUMERIC,
    FOREIGN KEY (userid) REFERENCES users(userid)
) '''

mycur.execute(create_table_2)

connection.commit()
connection.close()