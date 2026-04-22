class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
    
    # Using your logic: check if mid is in the "large" left half
            if nums[mid] > nums[r]: 
        # Target is even bigger than mid OR target is in the small right half
                if target > nums[mid] or target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
        # mid is in the "small" right half
        # Target is even smaller than mid OR target is in the large left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return ans