class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        new_stack = []
        i = 0
        median = 0
        j = 0
        while len(new_stack) != len(nums1)+len(nums2):
            if not nums1:
                new_stack = nums2
                break
            if not nums2:
                new_stack = nums1
                break
            
            if j < len (nums2)  :
                if nums1[i] > nums2[j]:
                    new_stack.append(nums2[j]) 
                    j+= 1
                else:
                    new_stack.append(nums1[i])
                    i += 1
            if j == len(nums2):
                j -=1 
                nums2[j] = max(nums1) +1

            if i == len(nums1):
                i -=1 
                nums1[i] = max(nums2) +1
        
        val = len(new_stack)%2
        l = 0
        h = len(new_stack) -1 
        if val != 0:
            median = new_stack[int((l+h)/2)]
        else:
            o = int((l+h)/2)
            median = (new_stack[o]+new_stack[o+1])/2

        return float(median)