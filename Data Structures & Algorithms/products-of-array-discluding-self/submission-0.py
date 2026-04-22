class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        map = defaultdict(int)
        for i in range(len(nums)):
            map[i] = 1

        for t,p in enumerate(nums):
            for c in range(len(nums)):
                if t == c:
                    continue
                map[t] *= nums[c]

        return list(map.values())
        

