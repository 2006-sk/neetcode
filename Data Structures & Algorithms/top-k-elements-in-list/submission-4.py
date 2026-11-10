class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(int)
        for r in nums:
            frequent[r] += 1
        result = []
        big = -1
        sorte = sorted(((c, n) for n, c in frequent.items()), reverse=True)

        for i in range(k):
            n, p = sorte[i]
            result.append(p)
        
        return result



            
