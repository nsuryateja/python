listOfFibo = [1,2]
limit = 4000000
firstNum = 1 
secondNum = 2
thirdNum = 0
while True:
        if not firstNum+secondNum < limit:
                break
        listOfFibo.append(firstNum+secondNum)
        thirdNum=firstNum 
        firstNum=secondNum
        secondNum=thirdNum+secondNum 
sumOfEven = 0        
for value in listOfFibo:
        if value%2==0:
                sumOfEven = sumOfEven + value
print(sumOfEven)
