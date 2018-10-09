import time
print('input length of the array')
lenArray = int(input())
listy = []
# This loop makes the list of ascending numbers starting from 1: range of each number being 1 to n-1...last two numbers are equal
for i in range(1,lenArray):
    listy.append(i)
listy.append(i)
#algo1
def returnDuplicate(lis):
    for x in range(len(lis)-1):
        for j in range(x+1,len(lis)):
            if lis[x]==lis[j]:
                return lis[x]
#algo2
def returnDuplicate2(lis):
    lis.sort()
    for x in range(1,len(lis)):
        if lis[x]==lis[x-1]:
            return lis[x]
new_list = []
#algo3
def returnDuplicate3(lis):
    for x in lis:
        if x not in new_list:
            new_list.append(x)
        else:
            return x
start = time.time()
a= returnDuplicate(listy)
end = time.time()
start1 = time.time()
b= returnDuplicate2(listy)
end1 = time.time()
start2 = time.time()
c= returnDuplicate3(listy)
end2 = time.time()
tim = end-start
tim1 = end1- start1
tim2 = end2 - start2
print('time taken is ' + str(tim) + ' secs' )
print('time taken is ' + str(tim1) + ' secs' )
print('time taken is ' + str(tim2) + ' secs' )
print('Algo 2 leads/lags the algo 1 by ' + str(abs(tim-tim1))+ ' secs')
print('Algo 3 leads/lags the algo 2 by ' + str(abs(tim2-tim1))+ ' secs')
print(str(a) + ' ' + str(b) + ' ' + str(c))

