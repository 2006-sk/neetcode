class Solution:
    def isValid(self, s: str) -> bool:
        hashma = { ')':'(', '}': '{', ']':'['}
        stack = []
        if len(s)%2 != 0:
            return False
        for e in s:
            if e in hashma:
                if not stack or stack[-1] != hashma[e]:
                    return False
                stack.pop() 
            else: 
                stack.append(e)
        return len(stack) == 0
