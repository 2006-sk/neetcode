class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        r =0
        profit = 0
        for i in range(len(prices)):
            r = i
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                ans = max(profit, ans)
            
            if prices[r] < prices[l]:
                l = r

        return ans