from collections import deque 
stack = deque()
brackets = {")": "(", "]": "[",  "}": "{"}
class Solution:
    def isValid(self, s: str) -> bool:
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not len(stack) == 0:
                    if stack[-1] == brackets[char]:
                        stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
