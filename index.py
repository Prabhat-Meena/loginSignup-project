from login import*

from signup import*

import json

user = input("Do you want to login or signup for login enter '1' or for signup enter '2' : ")

if user == '1':
    user_name = input("Enter your name : ")
    Email = input("Enter your Email-Id : ")
    password = input("Enter your pasword : ")
    print(login(user_name,Email,password))

elif user == '2':
    signup()

else:
    print(" you must enter 1 or 2 ")