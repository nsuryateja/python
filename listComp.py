def myfunc(stir):
    """Returns the string with upper-case letters at even places"""
    return ''.join([stir[x].lower() if x%2==0 else stir[x].upper() for x in range(len(stir))])
print(myfunc("passwhateveryouwanthere"))
