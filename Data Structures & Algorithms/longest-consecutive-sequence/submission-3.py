class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        map = defaultdict(int)
        for r in nums:
            map[r] += 1

        #Now we cna check for first value in nums in the map, if not found then we move ahead
        longest = 0
        for c in nums:
            length = 1
            if (c - 1) not in map:
                while (c +length) in map:
                    length+= 1
                longest = max(longest, length)
        return longest
            