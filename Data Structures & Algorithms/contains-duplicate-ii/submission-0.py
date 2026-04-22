class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #we use hashmap to store indices along with the value so we can get to check if indices difference
        hmap = defaultdict()

        for i in range(len(nums)):
            if nums[i] in hmap:
                val = abs(hmap[nums[i]]-i)
                if val <=k:
                    return True
            
            hmap[nums[i]] = i
        
        return False

    