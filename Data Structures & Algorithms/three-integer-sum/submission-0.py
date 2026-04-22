from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        n = len(nums)

        for i in range(n - 2):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = n - 1

            while L < R:
                tar = nums[i] + nums[L] + nums[R]

                if tar > 0:
                    R -= 1
                elif tar < 0:
                    L += 1
                else:
                    arr.append([nums[i], nums[L], nums[R]])

                    # move pointers after recording answer
                    L += 1
                    R -= 1

                    # skip duplicates at L
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    # skip duplicates at R
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

        return arr
