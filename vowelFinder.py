string = 'the fragrance of flowers spreads only in the direction of the wind'
lis = string.split()
print(lis)
vowel = 0
num = []
for i in range(len(lis)):
    k = lis[i]
    for r in k:
        if (r== 'a' or r== 'e' or r== 'i' or r== 'o' or r== 'u' ):
            vowel = vowel +1 
    num.append(vowel)
    vowel = 0
print(num)
high = tuple((num))
sett = max(high)
print(sett)
for item in range(len(lis)):
    if num[item] == sett:
        print(str(num[item])+' '+lis[item])
    
        


