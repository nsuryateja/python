def check(num,*args):
    for item in args:
        countUpper = 0
        countDigit = 0
        for i in item:
            if i.isupper():
                countUpper == countUpper +1
            if i.isdigit():
                countDigit == countDigit + 1
        if not countUpper >= 2 or countDigit != 3  or len(set(item)) != len(item) or len(item) != 10 or not item.isalpha():
            print("Invalid")
