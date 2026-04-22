class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        p = [0]*a
        seen  = set(
        )
        for x in nums:
            seen.add(x)
        if len(seen) != a:
            return True
        return False


        