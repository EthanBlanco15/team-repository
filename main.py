#secret passcode to be an admin
secret_passcode = "admin.py"

#list containing all login info
login_info = []

#list of remaining time slots
times_left = ["12:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00"]

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
            while True:
                breakout = True
                new_username = input("What do you want your username to be?\n-->")
                for account in login_info:
                    if new_username in account:
                        print("That username is already taken!")
                        breakout = False
                        break
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
            while True:
                admin_choice = input("Type 1 to become an admin and type 2 to create a normal account.\n-->")
                if admin_choice == "1":
                    passcode = input("What is the secret passcode to become an admin?\n-->")
                    if passcode == secret_passcode:
                        print("You are now an admin!")
                        if_admin = True
                        break
                    else:
                        print("Incorrect!")
                        print("Your account is set to normal.")
                        if_admin = False
                        break
                        #inputs info into database
                if admin_choice == "2":
                    print("Your account is set to normal.")
                    if_admin == False
                    break
                else:
                    print("Invalid input.")
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
                        num += 1
                        input_password = input("What is the password of your account?\n-->")
                        if input_password in account[1]:
                            login = True
                            accountloggedin = account
                            break
                        else:
                            print("Invalid password!")
                        

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
        choice = input("Type 1 if you want to schedule a new artist, \ntype 2 to remove a currently scheduled artist, \ntype 3 to modify a time that an artist is assigned to, \nand type 4 to exit schedule management.\n-->")
        if choice == "1":
            while True:
                tobreak = False
                print("Here are the available time slots:")
                times_left.sort()
                for time in times_left:
                    print(f"{time}")
                time_to_schedule = input("What time do you want to schedule? (Type exit to exit)\n-->")
                if time_to_schedule == "exit":
                    break
                for time in times_left:
                    if time_to_schedule == time:
                        times_left.remove(time)
                        artist_to_schedule = input(f"What is the name of the artist that you want to schedule to the time {time}?\n-->")
                        scheduled_artists.append((time, artist_to_schedule))
                        tobreak = True
                        break
                if tobreak:
                    break
                else:
                    print("That is not a valid time!")
        if choice == "2":
            while True:
                print("Here are the currently scheduled artists:")
                for item in scheduled_artists:
                    print(f"{item[0]}: {item[1]}")
                time_to_clear = input("Which time do you want to remove the artist from? (Type exit to exit)\n-->")
                testnum = 0
                for item in scheduled_artists:
                    if time_to_clear in item[0]:
                        times_left.append(item[0])
                        scheduled_artists.remove(item)
                        testnum += 1
                        break
                if testnum == 0:
                    print("There are no artists scheduled at that time!")
                    continue
                else:
                    break
        if choice == "3":
            while True:
                print("Here are the currently scheduled artists:")
                for item in scheduled_artists:
                        print(f"{item[0]}: {item[1]}")
                print("Here are the available time slots:")
                times_left.sort()
                for time in times_left:
                    print(f"{time}")
                num3 = 0
                choice_of_switch = input("Type 1 to switch an artist name or type 2 to switch a time of an artist?\n-->")
                if choice_of_switch == "1":
                    artist_to_change = input("What is the name of the artist that you want to change?\n-->")
                    for item in scheduled_artists:
                        if artist_to_change == item[1]:
                            new_artist_name = input("What do you want the artist's name to be now?\n-->")
                            scheduled_artists.append((item[0], new_artist_name))
                            scheduled_artists.remove(item)
                            num3 += 1
                            break
                    if num3 == 0:
                        print("There is not an artist scheduled by that name!")
                elif choice_of_switch == "2":
                    starthere = True
        if choice == "4":
            break

                    
                

                    


