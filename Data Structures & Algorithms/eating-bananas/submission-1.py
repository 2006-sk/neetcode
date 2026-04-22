class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        t = max(piles)
        l = 1
        newmin = t
        def finalhours(k:int) -> int:
            hrs =0
            for i in range(len(piles)):
                hrs += math.ceil(piles[i]/k)
            return hrs

        while l <= t:
            mid = (t+l)//2
            val = finalhours(mid)
            if val <= h:
                newmin = min(mid, newmin)
                t = mid -1
            else:
                l = mid + 1
        return int(newmin)
                