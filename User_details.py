#MODULES
import string
import random
def User():
    
    status = True
    container = []
    while status:
    #collection of data
        first_name = str(input("type in your first name.. \n"))
        last_name = str(input("type in your last name..\n"))
        email =  str(input("type in your email..\n"))
        full_name = ('Names: '+last_name + " " + first_name)
        User_email = (f"email: {email}")
        details =[full_name, User_email]

        
        #generating password for user
        rand = ''.join([random.choice(string.ascii_letters) for n in range (5)])
        code = first_name[:2] + last_name[-2:] + rand
        password = (f"password:  {code.lower()}")
        print (password)
        
                    
            #choice of password
        decide = str(input("type YES if you like the password or NO if you dont " ))
        if decide.lower() == "yes": 
            details.append(password)
            container.append(details)

        else:
            while decide.lower()!="yes":
                passd = str(input("type in your choice"))
                if len(passd) < 7:
                    print("not less than 7")

                elif " " in passd:
                    print("there is space in your password")

                else:
                    details.append(f" password: {passd}")
                    container.append(details)
                    break

         #new user       
        new_user = str(input("would you like to enter a new user? Yes or No"))
        if new_user.lower() == "no":
            status = False
            for info in container:
                print(info)
        else:
            status = True
      