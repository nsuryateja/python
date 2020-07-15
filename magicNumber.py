import random
magic_number = random.randint(0,10)
user_number = int(input("Enter a number between 0 and 10: "))
while not 0 <= user_number <= 10:
    user_number = int(input("Enter a number between 0 and 10: "))
print(magic_number)
if user_number == magic_number:
    print("MAGIC")
else:
    print("OOPS")
