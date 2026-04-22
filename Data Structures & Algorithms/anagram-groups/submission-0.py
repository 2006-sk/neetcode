from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def anagrams(n: str, t: str) -> bool:
            if len(n) != len(t):
                return False
            
            arr = list(n)
            for ch in t:
                if ch in arr:
                    arr.remove(ch)
                else:
                    return False   # IMPORTANT

            return len(arr) == 0

        arr2 = []
        visited = set()  # indices already grouped

        for i, n in enumerate(strs):
            if i in visited:
                continue

            arr1 = [n]
            visited.add(i)

            for j in range(i + 1, len(strs)):
                if j not in visited and anagrams(n, strs[j]):
                    arr1.append(strs[j])
                    visited.add(j)

            arr2.append(arr1)

        return arr2
