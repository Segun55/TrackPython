
import string
import random
def User():

    first_name = str(input("type in your first name.."))
    last_name = str(input("type in your last name.."))
    email =  str(input("type in your last email.."))
    full_name = ('Names: '+last_name + " " + first_name)
    User_email = ('email: ' + email)
    print(full_name)
    
    rand = ''.join([random.choice(string.ascii_letters) for n in range (5)])
    code = first_name[:2] + last_name[-2:] + rand
    password = ("password:  " + code.lower())
    print (password)

    decide = str(input("type yes if you like the password or no if you dont " ))
    if decide == "yes":
        print(full_name)
        print(User_email)
        print(password)
    else:
        while decide != "yes":
            passd = str(input("type in your choice"))
            if len(passd) > 9:
                print("not more than 9")
                
            elif len(passd) < 9:
                print("not less than 9")
                
            else:
                print(full_name)
                print(email)
                print(passd)
        else:
            pass