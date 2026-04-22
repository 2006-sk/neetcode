class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = []
        temp = []
        best = 0
        #loop

        newlist = sorted(nums)
        for i in range(len(newlist)):
            if arr == []:
                arr.append(newlist[i])
                best = 1
                continue
            diff = newlist[i] - newlist[i-1]
            if diff == 1:
                arr.append(newlist[i])
                
            elif diff == 0:
                continue
            
            else:
                arr = [newlist[i]]  # always restart

            if len(arr) > best:
                best = len(arr)
            
            
        return best


            
            