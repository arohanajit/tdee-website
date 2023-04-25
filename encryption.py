import getpass
import bcrypt

uname = input("Enter username: ")
pwd = getpass.getpass(prompt="Enter pwd: ")
pwd = pwd.encode('utf-8')
hashed_pwd = bcrypt.hashpw(pwd,bcrypt.gensalt())
print(hashed_pwd)