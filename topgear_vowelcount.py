text = """Python uses dynamic typing, and a combination of reference counting
and a cycle-detecting garbage collector for memory management.
It also features dynamic name resolution (late binding),
which binds method and variable names during program execution.
"""
helper = ''
for i in range(len(text)-1):
    if (text[i].isalpha() or text[i]== ' '):
        helper = helper + text[i]
    else:
        if text[i+1].isalpha():
            helper = helper+ ' '
        continue
print(helper)
lis = helper.split(' ')
print(lis)
vowel = 0
num = []
for i in range(len(lis)):
    k = lis[i]
    for r in k:
        if r in 'aeiou':
            vowel += 1 
    num.append(vowel)
    vowel = 0
sett = max(tuple((num)))
for item in range(len(lis)):
    if num[item] == sett:
        print(str(num[item])+' '+lis[item])
