spam =['apples','bananas','tofu','cats','hai','bye']
def returnString(spam):
    res = ''
    for item in range(len(spam)-1):
        res = res + spam[item] + ', '
    return res + 'and ' + spam[-1]
result = returnString(spam)
print(result)
