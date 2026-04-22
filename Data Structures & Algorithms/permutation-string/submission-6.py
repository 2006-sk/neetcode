class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        ##key idea is to compare window sizes and do such things but keep r moving forward.
        #issue is that if it is something like s1 = cab and s2 = llacacb, then acb gets true
        #lets try to get a frequency map, how to check if all
        #instead we can have a something
        #What my logic says to do is that we have a l and a r, r goes on, but if i is in map we bring l to that position, then we can add the
        #lets trya hashmap based approach
        #what if we just check if it is in s1, we add it to set, if not then. Otherwise we remove the value unitl value not in set then we move forward
        #eg would be s2:babcbcd s1:dc
        #@also clear hashset if a npc value comes then
        #Logic is fixed
        #A window of size 3, that checks if 3 chr combination from s1 to s2

        #hashmap, and variables l and r
        #move l if l-r > 2
    
        hmap = {chr(o): 0 for o in range(ord('a'), ord('z')+1)}#a to z asci
        for char in s1:
            hmap[char] += 1
#SHould contain all ltters not just found values
        n_map = {chr(t) : 0 for t in range(ord('a'), ord('z')+1)}
        l = 0
        for r in range(len(s2)):
            if r-l > len(s1)-1:
                n_map[s2[l]] -=1
                l += 1
            
            n_map[s2[r]] +=1
            if n_map == hmap:
                return True
        
        return False

            
            
            

    





