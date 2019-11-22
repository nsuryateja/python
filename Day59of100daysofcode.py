#Udemy Flask Tutorial Python level 2 OOP Exercise
class Account():
  def __init__(self,owner,bal = 0):
    self.owner = owner
    self.bal = bal

  def deposit(self,amount):
    self.bal += amount
    return self.bal
  #Cant withdraw more than balance...obvio!
  def withdraw(self,amount):
    if amount <= self.bal:
      self.bal -= amount
      print("self.bal")
    else:
      print("Error! No Bal")
  def __repr__(self):
    return "Owner: {}\nBalance: {}".format(self.owner,self.bal)

surya = Account("Surya")
print(surya)
surya.deposit(50)
print(surya.bal)
surya.withdraw(90)
print(surya.bal)

