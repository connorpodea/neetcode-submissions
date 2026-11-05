class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Interpret this as a 1D array. The logic remains the same
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            # Search the middle element
            m = (l + r) // 2

            # Since this is a 2D array, using division and modulo we
            # can find the appropriate row and column to search
            row = m // len(matrix[0])
            col = m % len(matrix[0])

            # Update the boundaries as normal
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        return False