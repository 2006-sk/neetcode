class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #It should start and end with a character from string t
        #lock when first character found, expand window to include second one, lock the second one as well
        #and after finding third one we measure length and change the window size
        l = 0
        h_map = Counter(t)
        length = len(h_map)
        count = False
        ans = [-1,-1]
        min = float('inf')
        def more(h_map):
            return all(value <= 0 for value in h_map.values())
        for r in range(len(s)):
            
            #new logic is I check if h_map the element exists if yes then incrment it by 1:,
            #we add a while loop and check for substrings, checnge window size and look for substrings
            if s[r] in h_map:
                
                h_map[s[r]] -= 1
            status = more(h_map)

            while status == True:
                if r-l +1 < min:
                    ans = [l,r]
                    min = r-l+1
                if s[l] in h_map:
                    h_map[s[l]] += 1
                l+= 1
                
                
                status = more(h_map)
            

                


                
        
        if ans == [-1,-1]:
            return ""
        else:
            return s[ans[0]:ans[1]+1]











