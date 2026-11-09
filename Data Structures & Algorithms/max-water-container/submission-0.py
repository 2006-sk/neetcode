class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        #my approach is going to be to be move whichever is smaller elft or right inward, do this until left == right
        maximum = 0
        left = 0
        right = len(nums)-1
        while left != right:
            if nums[left] < nums[right]:
                product = min(nums[left], nums[right]) * (right - left)
                
                maximum = max(maximum, product)
                
                left += 1
            else:
                product = min(nums[left], nums[right]) * (right - left)
                
                maximum = max(maximum, product)
                right -= 1
        return maximum


