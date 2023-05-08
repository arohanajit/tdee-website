from encryption import encrypt
from connection import connection_estb
from login_operation import add_row_uname, validation
from getpass import getpass
from tdee_operation import weight_cal_insert

def create_account(connection,mycur):
    result = encrypt()
    while result[0]=='invalid':
        result = encrypt()
    add_row_uname(connection,mycur,result)
    test_values = '''select * from users'''
    mycur.execute(test_values)
    print(mycur.fetchall())
    return result[0]

def login(connection,mycur):
    uname = ''
    while uname == '':
        credentials = ['','']
        credentials[0] = input("Enter username: ")
        credentials[1] = getpass(prompt="Enter pwd: ")
        uname = validation(connection,mycur,credentials)
        if uname == '':
            print("Username or Password wrong")
        else:
            print("Login Successful")
            return uname
    



if __name__ == "__main__":
    connection,mycur = connection_estb()
    choice = 0
    while choice!=3:
        choice = int(input("1. Create a new account\n 2. Log weight\n 3. Exit"))
        if choice==1:
            uname = create_account(connection,mycur)
            weight_cal_insert(connection,mycur,uname)
        elif choice==2:
            uname = login(connection,mycur)
            weight_cal_insert(connection,mycur,uname)
    connection.close()
      

    