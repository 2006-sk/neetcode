class Solution:
    def isPalindrome(self, s: str) -> bool:

        c = s.replace(' ', '')
        S = c.lower()
        S = ''.join(filter(str.isalnum, S))
        arr = list(S)

        L = 0
        R = len(arr) -1 
        #Start loop
        while R >= L:
            if arr[R] == arr[L]:
                R -= 1
                L += 1
                continue
            else:
                return False
        return True