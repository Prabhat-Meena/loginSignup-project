from signup import*

def login(user_name,Email,pasword):

    with open('user_info.json', 'r') as f:
        ac = json.load(f)
        if (user_name in ac and ac[user_name][0] == Email) :
            if ac[user_name][1] == pasword:
                return "login succesfull Hi", user_name
            else:
                return"incorect user name or pasword please try again"
        else:
            option = input('Incorect user name or pasword or you need to signup first for signup entere "y" or for login please enter "n" then try again : ')
            if option == "y":
                signup()
            else:
                return exit()