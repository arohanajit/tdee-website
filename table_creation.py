# Import the library
import pymysql

# Define the connection parameters for your AWS RDS database
host = "mysql-27d7cd4c-throaway81-71d1.k.aivencloud.com"  # Replace with your RDS endpoint
port = 12091  # Default MySQL port, change if you've configured a different port
user = "avnadmin"  # Replace with your RDS username
password = "AVNS_iGILA4XAwTt6zPCw-In"  # Replace with your RDS password
database = "defaultdb"  # Replace with your RDS database name

# Create a connection object
try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,  # Increase timeout if needed
        ssl = {'ca': '/Users/arohanajit/Documents/git-repos/tdee-website/Aiven MySQL CA.pem'}  # Path to your SSL certificate
    )
    
    with connection.cursor() as cursor:
        # Create username password table
        cursor.execute("SET SESSION sql_require_primary_key = 0")
        create_table_1 = '''
        CREATE TABLE IF NOT EXISTS users (
          userid VARCHAR(255) PRIMARY KEY,
          password VARCHAR(255),
          height NUMERIC,
          gender ENUM('M','F'),
          credential TEXT
        )'''
        cursor.execute(create_table_1)

        # Create values database linked by foreign key username
        create_table_2 = '''
        CREATE TABLE IF NOT EXISTS data (
            userid VARCHAR(255),
            date DATE,
            weight NUMERIC,
            calorie NUMERIC,
            FOREIGN KEY (userid) REFERENCES users(userid)
        ) '''
        cursor.execute(create_table_2)

    connection.commit()
    print("Tables created successfully!")

except pymysql.Error as e:
    print(f"An error occurred: {e}")

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Database connection closed.")