class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        se = set()
        l,r = 0,0
        if s == '':
            return 0
        if s == ' ':
            return 1
        for i in range(len(s)):
            r = i
            if s[i] in se:
                long = r-l
                ##if it i in se then i should remove that value from the sliding window
                while s[l] != s[r]:
                    se.remove(s[l])
                    l+= 1  
                l +=1
                ans = max(long, ans)
                continue
            
            se.add(s[r])
        ans = max(ans, r-l+1)
        return ans


        
       
