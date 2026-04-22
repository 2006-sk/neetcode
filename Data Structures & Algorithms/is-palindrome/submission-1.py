class Solution:
    def isPalindrome(self, s: str) -> bool:

        c = s.replace(' ', '')
        p = c.lower()
        S = ''
        for t in p:
            if ('a' <= t <= 'z') or ('0' <= t <= '9'):
                S += t

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