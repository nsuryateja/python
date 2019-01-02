while True:
    print('enter name and password')
    user=input()
    passw=input()
    if len(user)==7:
        print('length of the user name is 7')
        break
    elif passw.endswith('abc'):
        continue
    else:
        pass
print("broke out of the loop")
