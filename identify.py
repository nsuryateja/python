# Identifies the phone number of this pattern: 455-666-777
def identify(number):
    """Returns phone number or not"""
    if len(number) != 11:
        return "Not a Phone Number"
    if not (number[:3] + number[4:7] + number[8:]).isdecimal() and number[3] != '-' and number[7] != '-' and number[3] != '-' and number[7] != '-':
        return "Not a Phone Number"
    else:
        return "Yup! Phone Number"
print(identify("455-666-777"),identify("fhfgg"),identify("ccc-bbb-bbb"), sep = "\n")
