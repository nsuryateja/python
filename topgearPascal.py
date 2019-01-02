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
