import math
lis = []
def isPal(num):
        str1 = str(num)
        for i in range(len(str1)-1,-1,-1):
                lis.append(str1[i])
        stry = ''.join(lis)
        lis.clear()
        if str1 == str(stry):
                return True
        return False
mas = []
for i in range(999,0,-1):
        for j in range(999,0,-1):
              numb = i * j
              if isPal(numb)== True:
                   mas.append(numb)
print(max(mas))
