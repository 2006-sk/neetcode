class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #The question is askign me to go through the array, and find the values with lowest differences. and also eturn k amount of values.
        #If we try to sort int# get it in correct order ascending
        #Then stat a window now as it is sorted, window only contains smallest minus biggest, -1 and 0
        # So we go through all n values, check the differences, and on;y output the minimumDifference
        nums.sort()
        min = nums[-1] + 2
        l = 0
        for r in range(len(nums)):
            window = r-l+1
            if window == k:
                if nums[r] - nums[l] < min:
                    min = nums[r] - nums[l]
                l += 1
        return min



