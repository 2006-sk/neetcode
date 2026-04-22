class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sm = 0
        for b in weights:
            sm += b
        up = sm
        lp = max(weights)
        if up < lp:
            return lp
        
        def day_calc(midd):
            count = 0
            total = 0
            for i in weights:
                if total + i > midd:
                    count += 1
                    total = 0
                total += i
            return count
        while lp <= up:
            
            midd = (up+lp)//2
            mid = day_calc(midd)
            if mid >= days:
                lp = midd + 1
            else:
                up = midd - 1
        return lp

