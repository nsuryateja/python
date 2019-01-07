text = "hsida₹+₹-_((2!2!₹jsksm(₹(₹(ksksmdhkd"
helper = ''
for i in range(len(text)-1):
    if (text[i].isalpha() or text[i].isspace()):
        helper = helper + text[i]
    else:
        if text[i+1].isalpha():
            helper = helper+ ' '
        continue
print(helper)
listy = helper.split(' ')
print(listy)
