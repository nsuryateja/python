import sys
#Get the string from the file specified at the command line 
if len(sys.argv) > 1:
    filename = sys.argv[1]
with open('filename','r') as f:
        text = f.read()
#Create a helper string with only alphabets and spaces        
helper = ''        
for i in range(len(text)-1):
    if (text[i].isalpha() or text[i]== ' '):
        helper = helper + text[i]
    else:
        if text[i+1].isalpha():
            helper = helper+ ' '
        continue
#Create a list of all the individual words
lis = helper.split(' ')
#Count the no of vowels in each item and append the lengths in num list
vowel = 0
num = []
for i in range(len(lis)):
    k = lis[i]
    for r in k:
        if r in 'aeiou':
            vowel += 1 
    num.append(vowel)
    vowel = 0
#Get the maximum value out of the num list
sett = max(tuple((num)))
#Print the words which have maximum no of vowels ending with a new line
for item in range(len(lis)):
    if num[item] == sett:
        print(str(num[item])+' '+lis[item])
