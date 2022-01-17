import json

def signup():
    user_name = input("Enter your name: ")
    Email = input("Enter your Email-id: ")
    pasword = input("Enter your pasword: ")
    with open('user_info.json', 'r') as f:
        ac = json.load(f)
        if user_name in ac:
            print("user name is already taken you have to choose another user name and try again ")
            #option1 = input('Do you want to try again or want to exit for signup again enter "y" or for exit just press enter: ')
            #if option1 == "y":
            #    signup()
            #else:
            #    exit()
        else:
            ac[user_name] = [Email,pasword]

            ac = json.dumps(ac, indent=4)

            with open('user_info.json', 'w') as f:
                f.write(ac)
                print('Signup complete \nWelcom',user_name)