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
                        if user_input == 2:
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


    


#main function        
def main():
    artmanagment_backtrack = 0
    while True:
        selection = 0
        while selection < 1 or selection > 7:
            try:
                selection = int(input("\nWhere would you like to go?\n\n(1) Artist managment\n\n(2-5) WIP\n\n(6) Search for an artist\n\n(7) View all bands\n\nPlease type the number of your option: "))
                if selection > 3 or selection < 1:
                    print("\nPlease select only 1, 2, or 3\n")
            except:
                print("\nPlease only enter a whole number.")
        if selection == 1:
            if artmanagment_backtrack == 1:
                band_modify_func()
            else:
                add_band_func()
            artmanagment_backtrack = 1
        elif selection == 6:
            searcher_func()
        elif selection == 7:
            for i in range(len(dict_lists["lst_band_names"])):
                print(f"{dict_lists["lst_band_names"][i]} with artists {dict_lists["lst_artists"][i]} will be on stage {dict_lists["lst_venus"][i]} at {dict_lists["lst_timeslots"][i]} - Genres: {dict_lists["lst_genres"][i]}.")
        


#main runner
if __name__ == "__main__":
    main()