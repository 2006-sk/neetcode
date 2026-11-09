class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #If bigger than hi and lo and smaller than mid then between mid and lo, if bigger then between mid and hi, vice versa for smaller and also check hi lo in starting, it will kind od get to there. condition will be for index number

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:          # left half is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1               # target is in the sorted left half
                else:
                    lo = mid + 1               # target must be in the right half
            else:                              # right half is sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1               # target is in the sorted right half
                else:
                    hi = mid - 1               # target must be in the left half

        return -1

