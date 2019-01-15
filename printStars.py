#Prints the number of stars inputted onto the console...Recursion basic example
numOfStars = int(input("Input number of stars to print: "))
def recPrintStars(num):
    baseCase = "*"
    if num == 1:
        return baseCase
    else:
        return recPrintStars(num-1) + baseCase
print(recPrintStars(numOfStars))
