listOfFactors = []
def findFactors(num):
        for factor in range(2,num):
                if num% factor == 0:
                        listOfFactors.append(factor)
findFactors(600851475143) 
def isPrimeNumber(num):
        for i in range(2,num):
                if num% i == 0:
                        return False
        return True
for i in range(len(listOfFactors)-1,0,-1):
        if isPrimeNumber(listOfFactors[i])==True:
              print(listOfFactors[i])
              break
