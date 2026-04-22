from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        queue = deque()
        l = 0
        w_size = k
        for r in range(len(nums)):
            c_size = r-l+1
            
            while queue and nums[queue[-1]] < nums[r]:
                    queue.pop()
            queue.append(r)    
            if c_size >= w_size:
                
                if queue[0] < l:
                    queue.popleft()
                
                
            
            if (r + 1) >= k:
                ans.append(nums[queue[0]])
                l += 1
        return ans
                


            
            


