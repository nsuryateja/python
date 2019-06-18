#Giraffe language :replace vowels with g 
string = input('Enter a english word:')
listy = list(string)
vowel = ["a","e","i","o","u"]
for i in range(len(listy)):
    if listy[i] in vowel:
        listy[i] = "g"
print("".join(listy))
