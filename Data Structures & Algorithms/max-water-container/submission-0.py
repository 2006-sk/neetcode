class Solution:
    def maxArea(self, heights: List[int]) -> int:

        best = 0
        for i in range(len(heights)):
            
            j = len(heights) - 1
            if best == 0 :
                best = min(heights[i], heights[j]) * (j-i)
            #second loop
            while j > i:
                temp = min(heights[i], heights[j]) * (j-i)
                if temp > best:
                    best = temp
                j-=1
                continue
        return best