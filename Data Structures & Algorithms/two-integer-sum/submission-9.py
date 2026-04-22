class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = list()
        for i in range(0, len(nums) -1):
            
            tar = target - nums[i]
            
            for t in range(i+1, len(nums)):
                if tar == nums[t]:
                    arr.append(i)
                    arr.append(t)
                    return arr
            