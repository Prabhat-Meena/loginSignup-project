# imoprting user define loging and signup modules
from login import*

from signup import*

#import json
# taking input from users about what they want login or signup 
user_inp = input("Do you want to login or signup for login enter '1' or for signup enter '2' : ")
# checking condition accordig to user input
if user_inp == '1':
    user_name = input("Enter your name : ")
    Email = input("Enter your Email-Id : ")
    password = input("Enter your pasword : ")
    # calling login module/fuction which i imported to login
    print(login(user_name,Email,password))

elif user_inp == '2':
    # calling signup function which  i impored to signup
    signup()

else:
    # if the user gives a different input that does not meet any of the  conditions it will execute else
    print(" you must enter 1 or 2 ")