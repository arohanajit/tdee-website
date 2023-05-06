import getpass
import bcrypt

import re

def validate_password_input(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,}$'
    return bool(re.search(pattern, password))

def encrypt():
    uname = input("Enter username: ")
    pwd = getpass.getpass(prompt="Enter pwd: ")
    if(validate_password_input(pwd)):
        pwd = pwd.encode('utf-8')
        hashed_pwd = bcrypt.hashpw(pwd,bcrypt.gensalt())
        print(pwd,hashed_pwd)
        return [uname,hashed_pwd]
    else:
        return ['invalid','invalid']