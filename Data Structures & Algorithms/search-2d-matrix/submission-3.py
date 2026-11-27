class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        right = row_len * col_len - 1 

        while left <= right:
            
            mid = left + (right-left)//2 

            row = mid//col_len
            col = mid%col_len 

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid -1
            else:
                left = mid + 1

        return False 