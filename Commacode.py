#comma code
def listvalue(some):
    total=''
    for i in range(len(some)-1):
        if i==(len(some)-1):
            break
        total=total+some[i]+', '
    return total+ 'and ' + str(some[-1])
spam=['apples','bananas','tofu','cats','apples','bananas','tofu','cats']
print(listvalue(spam))
print(", ".join(spam[:-1]) + ', and '+spam[-1])
