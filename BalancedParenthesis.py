from collections import deque
strin = '(){}{}[][}}'
stack = deque()
def parrev(par):
  if par == ")":
    return "("
  if par == "]":
    return "["
  if par == "}":
    return "{"
def stringCal(strin):
  for char in strin:
    if char in '({[':
      stack.append(char)
    else:
      if not len(stack) == 0:
        if stack[-1] == parrev(char):
          stack.pop()
      else:
        return "FAIL"
  if len(stack) == 0:
    return "EXECUTED"
  else:
    return "FAIL"
print(stringCal(strin))
