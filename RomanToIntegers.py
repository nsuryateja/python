# CXDC(Reverse of given string) - 100 -10 + 500 -100 

Roman = {"I":1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}

inputString = "CDXC"
revString = inputString[::-1]

#Adding the first char
count = Roman[revString[0]]

#Add or Substract for 1 to last but one character
for char in range(1,len(revString) - 1):
      if Roman[revString[char]] < Roman[revString[char-1]]:
        count -= Roman[revString[char]]
      else:
        count += Roman[revString[char]]
        
#Add or Substract the last character        
count = count + Roman[revString[-1]] if revString[-1] > revString[-2] else count - Roman[revString[-1]]

#Print Integer Value
print(count)
