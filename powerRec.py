base = int(input("enter base value:"))
exponent = int(input("enter exponent value greater  than 2:"))
def power(base,exponent):
    if exponent == 2:
        return base*base
    else:
        return base*power(base,exponent-1)
print(power(base,exponent))
print(pow(base,exponent))
