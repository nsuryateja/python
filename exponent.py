#Prints out the exponent value eg: 2**3 = 8
base_value = int(input("enter base value:"))
power_value = int(input("enter power value:"))
val = base_value
for i in range(power_value-1):
    val = val * base_value
#Prints the result  
print(val)
#Comparing the result
print(base_value ** power_value)
