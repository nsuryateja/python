#Write a Python program which accepts the user's first and last name and print them in reverse order with a space 
# eg: input1: surya input2: teja output: ajet ayrus

def reverse(fstname,lstname):
    return lstname[::-1] + ' ' + fstname[::-1]
print('enter your first name:')
fstname = input()
print('enter your last name')
lstname = input()
print('Your full name in reverse: ')
print(reverse(fstname,lstname))
