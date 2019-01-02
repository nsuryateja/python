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
