from encryption import encrypt
from table_operation import connection_estb, add_row_uname, validation
from getpass import getpass

def create_account(connection,mycur):
    result = encrypt()
    while result[0]=='invalid':
        result = encrypt()
    add_row_uname(connection,mycur,result)
    test_values = '''select * from users'''
    mycur.execute(test_values)
    print(mycur.fetchall())

def login(connection,mycur):
    credentials = ['','']
    credentials[0] = input("Enter username: ")
    credentials[1] = getpass.getpass(prompt="Enter pwd: ")
    validation(connection,mycur,credentials)



if __name__ == "__main__":

    connection,mycur = connection_estb()
    # create_account(connection,mycur)
    login(connection,mycur)
    connection.close()
      

    