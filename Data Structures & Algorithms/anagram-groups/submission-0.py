from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #So my appoach is going to be Counter to get a hashmap and then compare it with counter of all the next values until we reach the end, we can use while as a condition. We need to maintain two counters and a result List and also create a 
        
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())



                
             



            
            
