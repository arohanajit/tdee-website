from encryption import encrypt
from connection import connection_estb
from login_operation import add_row_uname, validation
from getpass import getpass
from tdee_operation import weight_cal_insert, no_entry
import schedule
import time
import datetime

def create_account(connection,mycur):
    result = encrypt()
    while result[0]=='invalid':
        result = encrypt()
    if add_row_uname(connection,mycur,result)==1:
        test_values = '''select * from users'''
        mycur.execute(test_values)
        print(mycur.fetchall())
        weight_cal_insert(connection,mycur,result[0])
    else:
        print("Operation Failed")

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
            weight_cal_insert(connection,mycur,uname)
            break
    



if __name__ == "__main__":
    connection,mycur = connection_estb()
    schedule.every().day.at("23:50").do(no_entry, connection, mycur)
    choice = 0
    while choice!=3:
        choice = int(input("1. Create a new account\n2. Log weight\n3. Exit\nEnter: "))
        if choice==1:
            create_account(connection,mycur)
        elif choice==2:
            login(connection,mycur)
            
        schedule.run_pending()
        time.sleep(1)

    connection.commit()
    connection.close()
      

    