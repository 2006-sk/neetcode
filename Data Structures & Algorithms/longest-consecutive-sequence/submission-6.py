class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for start in s:
            if start - 1 not in s:        # start of a chain
                end = start
                while end in s:
                    end += 1
                best = max(best, end - start)

        return best
            