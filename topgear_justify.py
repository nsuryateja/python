import sys
if len(sys.argv)> 1:
        filename = sys.argv[1]
        width = sys.argv[2]
with open('filename','r') as f:
        text = f.read()
total = len(text)
def justify(text,width):
    helper = ''        
    for i in range(len(text)-1):
        if (text[i].isalpha() or text[i]== ' '):
            helper = helper + text[i]
        else:
            if text[i+1].isalpha():
                helper = helper+ ' '
            continue
    lis = helper.split(' ')
    new = []
    for i in lis:
        if i.isalpha():
             new.append(i)
    out = len(new)
    alpha = len(''.join(new))
    print('alphas '+str(alpha))
    print('total length  ' + str(total))
    justf = out-1
    print('no of words needed to justify ' + str(justf))
    spaces = total-alpha
    print('no of spaces ' + str(spaces))
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
    return res
print(justify(text,width))
