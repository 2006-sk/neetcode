class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h_set = set()

        for i in nums:
            if i in h_set:
                return i
            h_set.add(i)
