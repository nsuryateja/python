import sys
if len(sys.argv) > 1:
    heightOfPascal = sys.argv[1]
lisPascal =[]
for index in range(heightOfPascal-1):
    lisPascal.append([])
    for spaces in range(index+1):
        lisPascal[index].append(' ')
def appendListPascal(cur):
    if cur == 1:
        lisPascal[cur-1]=[1]
    elif cur == 2:
        lisPascal[cur-1]=[1,1]
    else:
        for val in range(cur):
            if val == 0 or val == cur-1:
                lisPascal[cur-1][val]=1
            else:
                lisPascal[cur-1][val]=lisPascal[cur-2][val-1]+lisPascal[cur-2][val]
for cur in  range(1,heightOfPascal):
    appendListPascal(cur)
for i in range(len(lisPascal)-1,-1,-1):
    for j in range(heightOfPascal- i-2):
        print('  ',end ='')
    for k in range(i+1):    
        print(lisPascal[i][k], end='   ')
    print('\n')
