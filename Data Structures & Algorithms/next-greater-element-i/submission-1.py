class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        for t,n in enumerate(nums1):
            hash[n] = t

        ans = [-1]*len(nums1)
        m_stack = []
        
        for i in range(len(nums2)):
            
            while m_stack and nums2[m_stack[-1]] < nums2[i]:
                val = nums2[m_stack.pop()]
                if val in hash:
                    ans[hash[val]] = nums2[i]
            m_stack.append(i)
        
        return ans