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
    """ends if \end is inputted** word exists in dictionary, prints the defination ** If it doesnt exist,gets the close finder """
    while True:
        user_input = input("Enter Word:").lower()
        if user_input == "\end":
            break
        if user_input in data.keys():
            print("\n".join(data[user_input]))
            continue
        user_input = "".join(close_finder(user_input))
        if user_input in data.keys():
            confirmation = input(f"Did you mean {user_input} instead? Y or N: ").lower()
            if confirmation == "y":
                print("\n".join(data[user_input]))
        else:
            print("Word doesn't exist")
data = data_loader()
translator()






