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
