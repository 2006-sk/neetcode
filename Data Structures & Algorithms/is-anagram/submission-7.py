class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        if len(s) != len(t):
            return False
        for i in t:
            if i in ss:
                ss.remove(i)
        
        if len(ss) == 0:
            return True
        return False