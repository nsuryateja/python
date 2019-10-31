#https://wipro.udemy.com/course/the-python-mega-course/learn/lecture/15702932#overview
#asks for the user input until the user inputs \end. if its a question, appends it with ? mnd also makes the first letter uppercase
listy = []
question = ("how","where","why","what","when")
while True:
  inp = input("Say something: ").lower()
  if inp == "\end":
    break
  for i in question:
    if inp.startswith(i):
      inp = inp[0].upper() + inp[1:] + "?"
      break
  else:
    inp = inp[0].upper() + inp[1:]
  listy.append(inp)
# sample output: What are you? How is your job? This is a great day
"""Inputs:
what are you
how is your job
this is a great day
"""
if len(listy) != 0:
  print(" ".join(listy))
