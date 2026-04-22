class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        high = (len(matrix)*len(matrix[0]))-1
        a = len(matrix[0])
        while low <= high:
            mid = (high+low)//2
            i = mid//a
            j= mid - a*i
            mid_val = matrix[i][j]
            if mid_val == target:
                return True
            elif mid_val > target:
                high = mid -1
            else:
                low = mid+1
        return False