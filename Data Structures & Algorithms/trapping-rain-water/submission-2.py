class Solution:
    def trap(self, height: List[int]) -> int:
        
        def nexthigh(L: int, height: List[int], R: int) -> int:
            largest = height[R]
            largest_index = R

            for c in range(R, len(height)):  # start at R itself
                if height[c] >= height[L]:
                    return c  # first bar that closes the container fully
                if height[c] > largest:
                    largest = height[c]
                    largest_index = c

            return largest_index  # tallest bar to the right if none reaches height[L]
      
                
        i = 0
        area = 0
        while i < len(height) - 1:
            j = i+1
            
            if height[i] == 0:
                i = j
                continue
            
            nums = nexthigh(i, height, j)
            if nums == (i+1):
                i = nums
                continue
            for t in range(i+1, nums):
                bound = min(height[i], height[nums])
                if height[t] < bound:
                    area += bound - height[t]

            i = nums

        return area
            

            
            
