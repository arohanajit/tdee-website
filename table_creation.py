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
  password VARCHAR(255)
)'''

mycur.execute(create_table_1)
test_values = '''insert into users values ('testuname','testpwd')'''
mycur.execute(test_values)

test_values = '''select * from users'''
mycur.execute(test_values)
mycur.fetchall()

# create values database linked by foreign key username
test_values = '''
CREATE TABLE data (
    userid VARCHAR(255),
    date DATETIME,
    weight NUMERIC,
    calorie NUMERIC,
    FOREIGN KEY (userid) REFERENCES users(userid)
) '''

mycur.execute(test_values)

test_values = '''insert into data values ('testuname',now(), 105, 2000)'''
mycur.execute(test_values)
test_values = '''select * from data'''
mycur.execute(test_values)
mycur.fetchall()

connection.commit()