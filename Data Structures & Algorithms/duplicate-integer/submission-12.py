class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sett = set()
        for i in nums:
            sett.add(i)

        if len(sett) != len(nums):
            return True

        return False