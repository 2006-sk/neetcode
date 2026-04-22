class Solution:
    def findMin(self, nums: List[int]) -> int:
         #This is a binary search range question. So array is sorted in ascending order and we don't know the number of times rotated.
         #What I can do is implement a binary search for a less than o(n) time complexity, min 0 rtaions amximum roation is size of array -1, because size of array brings to the same value again. 
         #how to change low and high now?
         # What if I can check with last [-1] which is o(1) lookup time. so if the value is smaller than -1, 
        l = 0
        h = len(nums)-1
         
        while h > l:
            mid = (h+l) // 2
            if nums[mid] > nums[-1]:
                l = mid +1
            else:
                h = mid
        
        return nums[h]