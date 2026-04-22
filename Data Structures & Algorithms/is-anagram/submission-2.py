class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        r = 0
        if len(t) != len(s):
            return False
        else:
            for i in s:
                arr.append(i)
                r += 1
            for p in t:
                if p in arr:
                    
                    arr.remove(p)
                    
            if not arr:
                return True
            else:
                return False
                
