# importing signup function so we can call the function with in login function
from signup import*

# importing json module so i can convert json data into python
import json 

def login(user_name,Email,password):
# openig json file in read mode.
    with open('user_info.json', 'r') as f:
        # converting json data into python.
        j_to_p = json.load(f)

        # condition to check user name or email exist or not in j_to_p.
        if (user_name in j_to_p and j_to_p[user_name][0] == Email) :
            
            # conditon to check password is correct or not
            if j_to_p[user_name][1] == password:
                return "login succesfull Hi", user_name
            else:
                return"incorect user name or password please try again"
        else:
            # taking input from user after if condition is false about users choice.
            option = input('Incorect user name or password or you need to signup first for signup entere "y" or for login please enter "n" then try again : ')
            if option == "y":
                signup()
            elif option == "n":
                return exit()
            else:
                return "you must enter y or n please try again"