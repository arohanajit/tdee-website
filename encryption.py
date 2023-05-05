import getpass
import bcrypt

import re

def validate_password(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,}$'
    return bool(re.search(pattern, password))

def main():
    uname = input("Enter username: ")
    pwd = getpass.getpass(prompt="Enter pwd: ")
    if(validate_password(pwd)):
        pwd = pwd.encode('utf-8')
        hashed_pwd = bcrypt.hashpw(pwd,bcrypt.gensalt())
        return [uname,hashed_pwd]
    else:
        return ['invalid','invalid']