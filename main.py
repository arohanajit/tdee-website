from encryption import encrypt
from connection import connection_estb
from login_operation import add_row_uname, validation
from getpass import getpass
from tdee_operation import weight_cal_insert, no_entry, tdee
from google_sheets import update_from_sheet
from calendar_event import create_event
import schedule
import time

def create_account(connection, cursor):
    result = encrypt()
    while result[0] == 'invalid':
        result = encrypt()
    if add_row_uname(connection, cursor, result) == 1:
        test_values = '''SELECT * FROM users'''
        cursor.execute(test_values)
        print(cursor.fetchall())
        weight_cal_insert(connection, cursor, result[0])
    else:
        print("Operation Failed")

def login(connection, cursor):
    uname = ''
    while uname == '':
        credentials = ['', '']
        credentials[0] = input("Enter username: ")
        credentials[1] = getpass(prompt="Enter pwd: ")
        uname = validation(cursor, credentials)
        if uname == '':
            print("Username or Password wrong")
        else:
            print("Login Successful")
            weight_cal_insert(connection, cursor, uname)
            # Calculate and display TDEE
            tdee_result = tdee(connection, cursor, uname)
            print(f"Your TDEE: {tdee_result[0]}")
            print(f"Your Average Weight: {tdee_result[1]}")
            print(f"Your Average Calories: {tdee_result[2]}")
            break

if __name__ == "__main__":
    connection, cursor = connection_estb()
    
    schedule.every().day.at("23:50").do(no_entry, connection, cursor)
    schedule.every().day.at("23:59").do(create_event, connection, cursor)
    schedule.every().hour.do(update_from_sheet, connection, cursor)
    
    choice = 0
    while choice != 3:
        choice = int(input("1. Create a new account\n2. Log weight\n3. Exit\nEnter: "))
        if choice == 1:
            create_account(connection, cursor)
        elif choice == 2:
            login(connection, cursor)
        
        create_event(connection, cursor)  # Pass both connection and cursor
        schedule.run_pending()
        time.sleep(1)

    connection.commit()
    connection.close()