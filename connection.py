import pymysql

def connection_estb():
    # Define the connection parameters
    # Define the connection parameters for your AWS RDS database
    host = "mysql-27d7cd4c-throaway81-71d1.k.aivencloud.com"  # Replace with your RDS endpoint
    port = 12091  # Default MySQL port, change if you've configured a different port
    user = "avnadmin"  # Replace with your RDS username
    password = "AVNS_iGILA4XAwTt6zPCw-In"  # Replace with your RDS password
    database = "defaultdb"  # Replace with your RDS database name

    # Create a connection object
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,  # Increase timeout if needed
        ssl = {'ca': '/Users/arohanajit/Documents/git-repos/tdee-website/Aiven MySQL CA.pem'}  # Path to your SSL certificate
    )
    mycur = connection.cursor()
    mycur.execute("SET time_zone = '+04:30'")
    connection.commit()

    return connection, mycur