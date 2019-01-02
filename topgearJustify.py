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
