import re
phoneNum = re.compile(r"\d{3}-\d{3}-\d{3}")
mo = phoneNum.search("dvhdsvhb45ms sbhbfdbfbfjhb888-888-888wbdhwbhdbc")
if mo != None:
    print(mo.group())
else:
    print("String has no phone number")
