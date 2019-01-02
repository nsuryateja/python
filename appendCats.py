cats=[]
while True:
    print('Enter the name of the cat '+str(len(cats)+1) + ' or nothing to stop')
    catName=input()
    if catName=='':
        break
    cats=cats+ [catName]#cats.append(catName)
print('cat names are')
for i in cats:
    print(' '+i)
