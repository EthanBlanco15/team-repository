#Ethan Blanco, Music Festival, Venue Management

venue_list = ("Nothing")

def venue_management(): #This function is for assigning stages with artists on a certain time for the music festival
    
    while True:
        venue_verifi = input(f"Is this done? Type yes or no to answer {venue_list}\n") #Lets the user see the current progress on the venue management
        if venue_verifi == "yes" and venue_verifi == "Yes" and venue_verifi == "YES": #As of right now, I am not sure why the "Yes" and "YES" don't work, it's probably my else statement though.
            print("Great! You should be done here now, if you haven't, try and see if all the other managements are done!")
            break
        elif venue_verifi == "no" and venue_verifi == "No" and venue_verifi == "NO":
            print("Let's get started then!")
            venue_start = input("""Would you like to create, edit, or remove an existing venue list?
                                1. Create a new venue list
                                2. Edit an already existing venue list
                                3. Remove a venue list
                                4. View venue list
                                5. Return/Backspace\n""") #Let's the user do what they want with the venue related stuff, anything that can be managed is available.
            if venue_start == "1":
                new_ven_name = input("What would you like to name this new venue list? Please include the name, stage and time.")
                venue_list = []
                venue_list.append(new_ven_name)
                venue_list.pop(1)
                print(venue_list)
            elif venue_start == "2":
                pass
            elif venue_start == "3":
                pass
            elif venue_start == "4":
                print("Here you go!")
                print(venue_list)
                continue
            elif venue_start == "5":
                print("Let's head back then, back to the start of the venue management!")
                continue
            else:
                print("This doesn't work, try entering a registered number instead!")
                continue
        elif venue_verifi == "" and venue_verifi == " ":
            print("You wrote nothing! Please try again.")
            continue
        else:
            print("This doesn't work, please try an appropriate options such as 'yes' or 'no' next time!")
            continue

def main():
    
    while True:
        #The main interface the user of this program will see
        user_interface = int(input("""Welcome to the Staff Music Festival! What would you like to work on?
                                1. Artist Management
                                2. Schedule Management
                                3. Venue Management
                                4. Ticket Sales
                                5. Search for functions, sales, attendees
                                6. All done
                                7. Exit\n"""))
        if user_interface == 1:
            pass
        elif user_interface == 2:
            pass
        elif user_interface == 3:
            venue_management()
        elif user_interface == 4:
            pass
        elif user_interface == 5:
            pass
        elif user_interface == 6:
            last_verifi = input("Are you sure you're done? Please reply with a simple yes or no\n")
            if last_verifi == "yes" and last_verifi == "Yes" and last_verifi == "YES":
                print("Thank you for your work today! It's time to head on home!")
                break
            elif last_verifi == "no" and last_verifi == "No" and last_verifi == "NO":
                print("It's time to head on back then!")
                continue
        elif user_interface == 7:
            print("Goodbye!")
            break
        else:
            print("This doesn't work, try again")
            continue
    return user_interface

main()