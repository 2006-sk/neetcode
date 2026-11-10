import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #formula is len(array) -k +1
        heap = []
        for i in nums:
            heapq.heappush( heap, i)
        
        looping = len(nums) - k

        for i in range(looping):
            heapq.heappop(heap)
        
        return heap[0]