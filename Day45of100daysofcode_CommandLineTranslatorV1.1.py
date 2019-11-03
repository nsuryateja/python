import json
import difflib

def data_loader():
    """Loads the data into dictionary from a JSON file"""
    with open("data.json") as f:
        data = f.read()
    return json.loads(data)

def close_finder(word):
    """Returns the close matches in the dictionary"""
    return difflib.get_close_matches(word,data_loader(),n=1)

def translator():
    """Checks for the respective definition in the dictionary and displays to the user"""
    while True:
        user_input = input("Enter Word: ").lower()
        if user_input == "\end":
            break
        #Checks for rain like words
        if user_input in data.keys():
            print("\n".join(data[user_input]))
            continue
        #Checks for India like words i.e., Proper nouns
        if user_input.title() in data.keys():
            print("\n".join(data[user_input.title()]))
            continue
        #Checks for USA like words i.e., Fullforms
        if user_input.upper() in data.keys():
            print("\n".join(data[user_input.upper()]))
            continue
        #Checks for close matches
        user_input = "".join(close_finder(user_input))
        if user_input in data.keys():
            while True:
                confirmation = input(f"Did you mean {user_input} instead? Y or N: ").lower()
                if confirmation == "y":
                    print("\n".join(data[user_input]))
                    break
                elif confirmation == "n":
                    print("Word doesn't exist")
                    break
                else:
                    print("We didn't understand your input! Sorry! Try again")
                    continue
        else:
            print("Word doesn't exist")
data = data_loader()
translator()






