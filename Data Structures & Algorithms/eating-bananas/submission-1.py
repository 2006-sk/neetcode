import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #I can define a fucntion that checks if Koko is able to complete the pile. 
        def time(rate):
            count = 0
            for r in piles:
                count += math.ceil(r/rate)
            return count

        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (hi+lo)//2

            if time(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        

        return lo

