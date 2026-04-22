class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L = 0
        R = len(numbers) - 1

        while L != R:
            val = numbers[L] + numbers[R]
            if val < target:
                L += 1
            if val > target:
                R -= 1
            if val == target:
                return[L+1, R+1]