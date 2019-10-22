#Project Day1
import pyperclip
print(pyperclip.paste())
inputString = pyperclip.paste()
listOfItems = inputString.split("\n")
def addstar(string):
    return "* " + string
print("\n".join([addstar(i) for i in listOfItems]))