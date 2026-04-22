class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = defaultdict(int)
        for i in nums:
            map[i] += 1
        S = set()
        value = list(map.values())
        value.sort(reverse=True)
        arr =[]
        for t in range(0,k):
            for c, v in map.items():
                if value[t] == v:
                    if c not in S:
                        arr.append(c)
                        S.add(c)
                        break
                    else:
                        continue
                    
        return arr


