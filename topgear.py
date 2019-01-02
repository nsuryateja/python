gd'''
name=''
while name!='your name':
    print('enter your name')
    name=input()
print('thanks')
'''
'''
isRunning=True
if isRunning==False:
    print('true')
elif not isRunning==True:
    print('fls')
else:
    print('do it')
'''
name='Alice'
age=42
if name=='Alice':
    print('Hi Alice!')
elif age<4:
    print('surya')
else:
    pass
while True:
    print('enter name and password')
    user=input()
    passw=input()
    if len(user)==7:
        print('length of the user name is 7')
        break
    elif passw.endswith('a'):
        continue
    else:
        pass
print("broke")
*********************************************************************************************annoying.py
def listvalue(some):
    total=''
    for i in range(len(some)-1):
        if i==(len(some)-1):
            break
        total=total+some[i]+', '
    return total+ 'and ' + str(some[-1])
spam=['apples','bananas','tofu','cats','pples','bananas','tofu','cats']
print(listvalue(spam))
*********************************************************************************************commacode.py
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
#print(name)
***********************************************************************************************demo.py
print('Hi there!!Please enter your name')
userName=input()
print(f'hi {userName} please enter your age')
print('hi {} please enter your age'.format(userName))
userAge=int(input())
print('you will be ' + str(userAge + 1)+ ' in a year')
***********************************************************************************************hello.py
print('hello')
print('please enter your name')
userInput=input()
print('Hi Mr.'+userInput)
print('enter your age')
userAge=input()
print('your age will be '+str(int(userAge)+1)+' in a year')
***********************************************************************************************hello1.py
text = 'python  code        '
total = len(text)
lis = text.split(' ')
print(lis)
new = []
for i in lis:
    if i.isalpha():
         new.append(i)
print(new)
out = len(new)
alpha = len(''.join(new))
print('alphas '+str(alpha))
print('total length  ' + str(total))
justf = out-1
print('no of words needed to justify ' + str(justf))
spaces = total-alpha
print('no of spaces ' + str(spaces))
#for i in range(len(lis)-1):
res = []
for i in range(len(new)-1):
    res.append(new[i])
    if not spaces/justf-spaces//justf == 0:
        res.append(spaces//justf + 1)
        spaces = spaces - (spaces//justf + 1)
    else:
        res.append(spaces//justf)
        spaces = spaces - (spaces // justf)
    justf = justf - 1
res.append(new[len(new)-1])
print(res)
***********************************************************************************************justify.py
listy = []
for i in range(1,10100000):
    listy.append(i)
    listy.append(i)
listLengthBefore = len(listy)
print('length of the list before '+ str(listLengthBefore))
def removeDuplicates(listy):
    count = 0
    for i in range(len(listy)-1):
        if listy[i]==listy[i+1]:
            count = count  +1
    return count
lenOfArray = removeDuplicates(listy)
print('length of list after '+ str(lenOfArray))
print('No of duplicate elements are '+ str(listLengthBefore-lenOfArray))
***********************************************************************************************pyth1.py
listy = [0,0,1,1,1,2,2,3,3,4]
inn = []
for i in range(len(listy)-1):
    if listy[i]==listy[i+1]:
        inn.append(i)

print('List of indices of duplicate numbers')
print(inn)
new = []
for i in range(len(inn)):
    res = inn[i]
    new.append(listy[res])
print('Duplicate elements')
print(new)
hymn = []
for i in range(len(listy)):
    if i in inn:
        continue
    else:
        hymn.append(listy[i])
print('list after removing duplicates')
print(hymn)
***********************************************************************************************pyth2.py
#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")
***********************************************************************************************pyth3.py
def fibo(n):
    if n==1 or n==2:
        return 1
    else:

        return fibo(n-1)+fibo(n-2)
print(fibo(28))
fib = {}
def fibonacci(n):
    if n in fib.keys():
        return fib[n]
    elif n==1 or n==2:
        return 1
    else:
        val = fibonacci(n-1)+fibonacci(n-2)
        return val
    fib[n]=val
print(fibonacci(28))
***********************************************************************************************recAndMemorization.py
spam =['apples','bananas','tofu','cats','hai','bye']
def returnString(spam):
    res = ''
    for item in range(len(spam)-1):
        res = res + spam[item] + ', '
    return res + 'and ' + spam[-1]
result = returnString(spam)
print(result)
***********************************************************************************************returnString.py
import trend2
lists = ['tuna','bacon','ham','sausage']
for f in range(len(lists)):
    stri = lists[f]  # 'tuna'
    lent = len(stri) # 4
    lists[f]= stri[:lent-1]+ str(lent)# lists[0] = 'tun' + 4
print(lists)
stry=trend2.matchStr('surya',' teja')
***********************************************************************************************strings.py
tableData= [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]
for i in range(len(tableData[0])):
      for j in range(len(tableData)):
             print(tableData[j][i].rjust(8),end ='')
      print('\n')
***********************************************************************************************tabledata.py
pascal = [1,1]
height = int(input('height of pascal structure?'))
for i in range(height+2):
    pascal.append(None)
    print(' ',end='')
print('1')
for i in range(height):
    print(' ',end='')
print('1   1')
for i in range(height-2):
    for j in range(height-i-2):
        print(' ',end='')
    print('1',end='')
    cur =1
    prev = 1
    while(not pascal[cur]==None):
        print('   ',end='')
        value= prev + pascal[cur]
        prev = pascal[cur]
        pascal[cur] = value
        print(value,end='')
        cur = cur + 1
        if cur == height:
            break
    print('   1')
    if not pascal[-1]==None:
        break
    pascal[cur] = 1
   # print('\n')
   # print(pascal)
***********************************************************************************************topgearPascal.py
name1='samsung galaxy g4'
name2='samsung galaxy g2'
name3='battle of thrones'
name4='savitor the flash in the season last'
name5='donning it in style'
name6='style donning it in'
def matchString(str1,str2):
    lst1=str1.split()
    lst2=str2.split()
    lst1.sort()
    lst2.sort()
    print('return values are ')
    if len(str1)>25:
        return 0
    elif len(str2)>25:
        return 1
    elif lst1==lst2:
        return 2
    else:
        return 3
def matchStr(str3,str4):
    print(str3+str4)
returnVal1=matchString(name1,name2)
returnVal2=matchString(name3,name4)
returnVal3=matchString(name5,name6)
***********************************************************************************************trend2.py
