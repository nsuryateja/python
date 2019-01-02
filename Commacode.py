def listvalue(some):
    total=''
    for i in range(len(some)-1):
        if i==(len(some)-1):
            break
        total=total+some[i]+', '
    return total+ 'and ' + str(some[-1])
spam=['apples','bananas','tofu','cats','pples','bananas','tofu','cats']
print(listvalue(spam))
