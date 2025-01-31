# dict_lists is a dictionary that holds multiple lists, including band names, artists, venues, timeslots, and genres.
# lst_band_names is a list that stores the name of each band.
# lst_artists is a list that stores all the names of the artists that belong to a band.
# lst_venus is a list that stores the venues where the bands will perform.
# lst_timeslots is a list that stores the time slots for the band's performances at the respective venues.
# lst_genres is a list that stores the genres of music each band will be playing.
# band is a temporary variable used to store the name of a band during the addition of bands.
# artists is a temporary variable used to store the names of artists in a band.
# venue is a temporary variable used to store the venue for a band's performance.
# time is a temporary variable used to store the performance time of a band.
# genres is a temporary variable used to store the genres a band will play.
# artmanagment_backtrack is used to track whether it's the user's first time managing bands, with different functionality based on the value.
# selection is a temporary variable used for user input to select an action during different steps of the program.
# found_indexes is a list used to store the indexes of bands that match a search term.
# choice is a temporary variable used to select an option for modifying a band.
# search_term is a variable used to store the term inputted by the user for searching through bands.
# found is a boolean flag used to track if any matching bands were found during a search.


#these lists are created outside any functions so that everyone is able to use them

dict_lists = {
    "lst_band_names": [],
    "lst_artists": [],
    "lst_venus": [],
    "lst_timeslots": [],
    "lst_genres": []
}
  

def add_band_func():
    num_bands = 0
    while num_bands == 0:
        num_bands = (input("\nHow many bands would you like to add? "))
        try:
            num_bands = int(num_bands)
        except:
            print("\nplease only enter a whole number")
            num_bands = 0
    for i in range(num_bands):
        band = input(f"\nEnter the name of band {i+1}: ")
        artists = input(f"\nEnter the artists in {band} (format: artist1, artist2, artist3): ")
        venue = input(f"Which venu will {band} be preforming at? ")
        time = input(f"\nWhat time will {band} perform on stage {venue}? (format: [][]:[][] AM/PM) ")
        genres = input(f"\nWhich genres will {band} be playing? (format: Jazz, Electronic, Rock):  ")
          
        dict_lists["lst_band_names"].append(band)
        dict_lists["lst_artists"].append(artists)
        dict_lists["lst_venus"].append(venue)
        dict_lists["lst_timeslots"].append(time)
        dict_lists["lst_genres"].append(genres)

    # Display added bands
    print("\n--- Bands Added ---")
    for i in range(len(dict_lists["lst_band_names"])):
        print(f"{dict_lists["lst_band_names"][i]} with artists {dict_lists["lst_artists"][i]} will be on stage {dict_lists["lst_venus"][i]} at {dict_lists["lst_timeslots"][i]} - Genres: {dict_lists["lst_genres"][i]}.")

#this allows modification, deletion, and creation of new lists
def band_modify_func():
    selection = 0
    selection = int(selection)
    while selection < 1 or selection > 2:
        selection = int(input(f"We detect that you have already made {len(dict_lists["lst_band_names"])} band lists.\n\nYou can:\n\n(1) Modify an already existing band list\n\n(2) Delete you band list(start over)\n\n(3) Go back to main menu\n\nPlease type the number corrosponding to your selectoin: "))
        if selection == 1:
            search_term = input("Enter the band name, artist name, stage, time slot, or genre to modify: ").strip().lower()
            found_indexes = []

            for i in range(len(dict_lists["lst_band_names"])):
                band_name = dict_lists["lst_band_names"][i].lower()
                artist_names = dict_lists["lst_artists"][i].lower()
                venue = dict_lists["lst_venus"][i].lower()
                time_slot = dict_lists["lst_timeslots"][i].lower()
                genre = dict_lists["lst_genres"][i].lower()

                if (search_term in band_name or search_term in artist_names or search_term in venue or search_term in time_slot or search_term in genre):
                    print(f"\n{i+1}. {dict_lists["lst_band_names"][i]} with artists {dict_lists["lst_artists"][i]} will be on stage {dict_lists["lst_venus"][i]} at {dict_lists["lst_timeslots"][i]} - Genres: {dict_lists["lst_genres"][i]}")
                    found_indexes.append(i)

            if not found_indexes:
                print("\nNo matching bands found.")
                return

            if len(found_indexes) > 1:
                selection = int(input("\nMultiple matches found. Enter the number corresponding to the band you want to modify: ")) - 1
            else:
                selection = found_indexes[0]

            while True:
                print("\nWhat would you like to modify?")
                print("1. Band Name\n2. Artists\n3. Stage\n4. Time Slot\n5. Genre\n6. Go back")
                choice = int(input("Enter the number corresponding to your choice: "))

                if choice == 1:
                        dict_lists["lst_band_names"][selection] = input("Enter the new band name: ").strip()
                elif choice == 2:
                    dict_lists["lst_artists"][selection] = input("Enter the new artists (format: artist1, artist2, artist3): ").strip()
                elif choice == 3:
                    dict_lists["lst_venus"][selection] = input("Enter the new stage: ").strip()
                elif choice == 4:
                    dict_lists["lst_timeslots"][selection] = input("Enter the new time slot: ").strip()
                elif choice == 5:
                    dict_lists["lst_genres"][selection] = input("Enter the new genres (format: genre1, genre2): ").strip()
                elif choice == 6:
                    break
                else:
                    print("\nInvalid choice. Please try again.")
        elif selection == 2:
            while True:
                try:
                    if int(input("ARE YOU SURE YOU WANT TO DELETE YOUR BAND LIST?\n\n(1) no\n\n(2) yes\n\nType the number corresponding to your selection: ")) == 2:
                        dict_lists["lst_band_names"] = []
                        dict_lists["lst_artists"] = []
                        dict_lists["lst_venus"] = []
                        dict_lists["lst_timeslots"] = []
                        dict_lists["lst_genres"] = []
                        break
                    else:
                        break
                except:
                    print("Please only input a whole number")

        elif selection == 3:
            break


def searcher_func():
    while True:
        try:
            if int(input("Would you like to search for a spesific artist, or be recomended one bassed off of inputed genres?\n\n(1) Search\n\n(2) Our recomendation\n\n Type the number corrosponding to your selection: ")) == 1:
                search_term = input("Enter the term you want to search for (Band Name, Artist, Venue, Time Slot, Genre): ").strip().lower()
                found = False

                for i in range(len(dict_lists["lst_band_names"])):
                    band_name = dict_lists["lst_band_names"][i].lower()
                    artist_names = dict_lists["lst_artists"][i].lower()
                    venue = dict_lists["lst_venus"][i].lower()
                    time_slot = dict_lists["lst_timeslots"][i].lower()
                    genre = dict_lists["lst_genres"][i].lower()

                    # Check if search term matches any field
                    if (search_term in band_name or search_term in artist_names or
                        search_term in venue or search_term in time_slot or search_term in genre):
                        print(f"\n{dict_lists["lst_band_names"][i]} with artists {dict_lists["lst_artists"][i]} will be on stage {dict_lists["lst_venus"][i]} at {dict_lists["lst_timeslots"][i]} - Genres: {dict_lists["lst_genres"][i]}.")
                        found = True

                if not found:
                    print("\nNo matching bands found.")
            else:
                search_term = input("Enter the genre(s) you want to search for (e.g., 'Jazz', 'Rock, Electronic'): ").strip().lower()

                found_indexes = []  

                for i in range(len(dict_lists["lst_band_names"])):
                    genres = dict_lists["lst_genres"][i].lower()  

                    
                    genre_list = genres.split(",") 
                    for genre in genre_list:
                        if search_term in genre.strip():  
                            found_indexes.append(i)
                            break  

                if found_indexes:
                    print("\nMatching bands found based on genre(s):")
                    for i in found_indexes:
                        print(f"{dict_lists['lst_band_names'][i]} with artists {dict_lists['lst_artists'][i]} will be on stage {dict_lists['lst_venus'][i]} at {dict_lists['lst_timeslots'][i]} - Genres: {dict_lists['lst_genres'][i]}")
                else:
                    print("\nNo matching bands found.")
                break
        except:
            print("\nPlease enter in a whole number.")

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

#importing random
import random

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
                    while True:
                        num2 = 0
                        time_to_change = input("What is the time that you want to change? (Type exit to exit)\n-->")
                        for item in scheduled_artists:
                            if time_to_change == item[0]:
                                while True:
                                    num4 = 0
                                    new_time = input("What is the time that you want to change to? (Type exit to exit)\n-->")
                                    for time in times_left:
                                        if new_time == time:
                                            scheduled_artists.append((new_time, item[1]))
                                            times_left.append(item[0])
                                            times_left.remove(new_time)
                                            scheduled_artists.remove(item)
                                            num4 +=1
                                    if new_time == "exit":
                                        break
                                    if num4 == 0:
                                        print("That is not a time that is left.")
                                        print("Here are the available time slots:")
                                        times_left.sort()
                                        for time in times_left:
                                            print(f"{time}")
                                    else:
                                        break
                                num2 += 1
                        if time_to_change == "exit":
                            break
                        if num2 == 0:
                            print("There are no artists scheduled for that time!")
                            print("Here are the currently scheduled artists:")
                            for item in scheduled_artists:
                                    print(f"{item[0]}: {item[1]}")
                        else:
                            break
        if choice == "4":
            break
        else:
            print("That is not valid option!")


venue_list = set({})

def venue_management(venue_list): #This function is for assigning stages with artists on a certain time for the music festival
    
    while True:
        venue_verifi = input(f"Is this done? Type yes or no to answer {venue_list}\n") #Lets the user see the current progress on the venue management
        if venue_verifi == "yes" or venue_verifi == "Yes" or venue_verifi == "YES":
            print("Great! You should be done here now, if you haven't, try and see if all the other managements are done!")
            break
        elif venue_verifi == "no" or venue_verifi == "No" or venue_verifi == "NO":
            print("Let's get started then!")
            venue_start = int(input("""Would you like to create, edit, or remove an existing venue list?
                                1. Create a new venue list
                                2. Edit an already existing venue list
                                3. Remove a venue list
                                4. View venue list
                                5. Return/Backspace
                                6. Exit\n""")) #Let's the user do what they want with the venue related stuff, anything that can be managed is available.
            if venue_start == 1: #Lets the user add a new list
                new_ven_name = input("What would you like to name this new venue list? Please include the name for the artist\n")
                venue_list.add(new_ven_name)
                print(venue_list)
            elif venue_start == 2: #Lets the user edit any existing list
                edit_ven_name = input(f"What would you like to edit? Please enter a list that already exists {venue_list}\n")
                venue_list.discard(edit_ven_name)
                editing_ven_name = input("Now what's the new name?")
                venue_list.add(editing_ven_name)
                print(venue_list)
            elif venue_start == 3: #Lets the user remove any existing list
                remove_ven_name = input(f"What would you like to remove? Please enter a list that already exists {venue_list}\n")
                venue_list.discard(remove_ven_name)
                print(venue_list)
            elif venue_start == 4: #Viewing the list anytime
                print("Here you go!")
                print(venue_list)
                continue
            elif venue_start == 5: #Backtracking
                print("Let's head back then, back to the start of the venue management!")
                continue
            elif venue_start == 6: #Exit for the player anytime
                print("Goodbye!")
                break
            else:
                print("This doesn't work, try entering a registered value instead!") #Error handling
                continue
        elif venue_verifi == "" or venue_verifi == " ": #For blank responses
            print("You wrote nothing! Please try again.")
            continue
        else:
            print("This doesn't work, please try an appropriate options such as 'yes' or 'no' next time!")
            continue #For any other type of invalid input

#Ticket Sales and Attendee Management Function
def ticket_sales():
    while True:
        choice = input("Type 1 to add a ticket, type 2 to remove a ticket, and type 3 to exit.\n-->")
        if choice == "1":
            while True:
                type_of_ticket = input("Type 1 to add a 1-day ticket, type 2 to add a 3-day ticket, type 3 to add a VIP ticket, and type 4 to exit.\n-->")
                if type_of_ticket == "1":
                    name_for_ticket = input("What is the name of the owner of the ticket?\n-->")
                    ticket_num_list = []
                    for i in range(10):
                        ticket_num_list.append(random.randint(0,9))
                    ticket_num = "".join(ticket_num_list)
                    print("Here is your ticket (Remember the ticket number!!!):")
                    tickets.append((name_for_ticket, "1-day", ticket_num))
                    print((name_for_ticket, "1-day", ticket_num))
                    break
                elif type_of_ticket == "2":
                    name_for_ticket = input("What is the name of the owner of the ticket?\n-->")
                    ticket_num_list = []
                    for i in range(10):
                        ticket_num_list.append(random.randint(0,9))
                    ticket_num = "".join(ticket_num_list)
                    print("Here is your ticket (Remember the ticket number!!!):")
                    tickets.append((name_for_ticket, "3-day", ticket_num))
                    print((name_for_ticket, "3-day", ticket_num))
                    break
                elif type_of_ticket == "3":
                    name_for_ticket = input("What is the name of the owner of the ticket?\n-->")
                    ticket_num_list = []
                    for i in range(10):
                        ticket_num_list.append(int(random.randint(0,9)))
                    ticket_num = "".join(ticket_num_list)
                    print("Here is your ticket (Remember the ticket number!!!):")
                    tickets.append((name_for_ticket, "VIP", ticket_num))
                    print((name_for_ticket, "VIP", ticket_num))
                    break
                else:
                    print("Not a valid ticket type!")
        elif choice == "2":
            while True:
                num5 = 0
                print("These are all of the tickets:")
                for ticket in tickets:
                    print(ticket)
                ticket_num_to_delete = input("What is the ticket number to delete? (Type exit to exit)\n-->")
                for ticket in tickets:
                    if ticket_num_to_delete == ticket[2]:
                        tickets.remove(ticket)
                        num5 += 1
                if ticket_num_to_delete == "exit":
                    break
                if num5 == 0:
                    print("No tickets with that ticket number!")
                else:
                    break
        elif choice == "3":
            break
                
def main():
    artmanagment_backtrack = 0
    while True:
        #The main interface the user of this program will see
        user_interface = int(input("""Welcome to the Staff Music Festival! What would you like to work on?
                                1. Artist Management
                                2. Schedule Management
                                3. Venue Management
                                4. Ticket Sales
                                5. Search for functions, sales, attendees
                                6. All done\n"""))
        if user_interface == 1:
            if artmanagment_backtrack != 1:
                add_band_func()
                artmanagment_backtrack = 1
            elif artmanagment_backtrack == 1:
                band_modify_func(artmanagment_backtrack)
        elif user_interface == 2:
            schedule_management()
        elif user_interface == 3:
            venue_management(venue_list)
        elif user_interface == 4:
            ticket_sales()
        elif user_interface == 5:
            pass
        elif user_interface == 6: #Completely exists out of the program with a "are you sure?" question.
            last_verifi = input("Are you sure you're done? Please reply with a simple yes or no\n")
            if last_verifi == "yes" or last_verifi == "Yes" or last_verifi == "YES":
                print("Thank you for your work today! It's time to head on home!")
                break
            elif last_verifi == "no" or last_verifi == "No" or last_verifi == "NO":
                print("It's time to head on back then!")
                continue
    return user_interface

if __name__ == "__main__":
    main()
