# Identifies the phone number of this pattern: 455-666-777
def identify(number):
    """Returns phone number or not"""
    if len(number) != 11:
        return False
    elif (number[:3] + number[4:7] + number[8:]).isdecimal() and number[3] + number[7] == "--":
        return True
    else:
        return False
print(identify("455-666-777"), identify("rn: 455-666"), identify("ccc-bbb-bbb"), sep="\n")
def chunks(chunk):
    for i in range(len(chunk) - 10):
        text = chunk[i:i + 11]
        if identify(text):
            return text + " is the phone number"
    return "No phone number in given string"
print(chunks("Identifies the phone number of this pattern: 455-666-777"))



