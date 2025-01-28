#secret passcode to be an admin
secret_passcode = "admin.py"

#list containing all login info
login_info = []

#list of remaining time slots
times_left = ["12:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00"]

#list of all currently scheduled artists
scheduled_artists = []

#list of all tickets
tickets = []

#sign-in/sign-up function
def sign_in():
    while True:
        choice = input("Type 1 to sign-up, type 2 to login, type 3 if you want to exit.\n-->")
        
        #choice to sign-up
        if choice == "1":
            #checks if the username is taken
            breakout = True
            while True:
                new_username = input("What do you want your username to be?\n-->")
                for account in login_info:
                    if new_username in account:
                        print("That username is already taken!")
                        breakout = False
                if breakout:
                    break

            #password input
            while True:
                new_password = input("What do you want your password to be?\n-->")
                confirm_password = input("Type password again to confirm.\n-->")
                if new_password == confirm_password:
                    break
                else:
                    print("Passwords do not match!")

            #choice to become an admin
            admin_choice = input("Type 1 to become an admin and type 2 to create a normal account.\n-->")
            if admin_choice == "1":
                passcode = input("What is the secret passcode to become an admin?\n-->")
                if passcode == secret_passcode:
                    print("You are now an admin!")
                    if_admin = True
                else:
                    print("Incorrect!")
                    print("Your account is set to normal.")
                    if_admin = False
                    #inputs info into database
            login_info.append((new_username, new_password, if_admin))
            print("Account created successfully!")
        
        #choice to login
        if choice == "2":
            while True:
                login = False
                num = 0
                input_username = input("What is the username of your account?\n-->")

                #checks if the username is in the database
                for account in login_info:
                    if input_username in account:
                        #checks if the password correlates to the username
                        input_password = input("What is the password of your account?\n-->")
                        if input_password in account[1]:
                            login = True
                            accountloggedin = account
                            break
                        else:
                            print("Invalid password!")
                        num += 1

                if num == 0:
                    print("No account with that username!")
                    continue

                if login:
                    print("Login successful!")
                    return accountloggedin
        
        #choice to exit system
        if choice == "3":
            return "exit"

        else:
            print("Not a valid input!")

#schedule management function
def schedule_management():
    while True:
        choice = input("Type 1 if you want to")

                    


