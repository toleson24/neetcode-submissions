class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row, t, lo, hi): 
            if lo > hi:
                return False
            
            mid = lo + (hi - lo) // 2

            if row[mid] == t:
                return True
            elif row[mid] > t:
                return binarySearch(row, t, lo, mid - 1)
            else: # row[mid] < t
                return binarySearch(row, t, mid + 1, hi)
            
            return False

        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        def rowSearch(mat, t, lo, hi): 
            if lo > hi:
                return -1 
            
            mid = lo + (hi - lo) // 2

            if mat[mid][0] <= t <= mat[mid][-1]:
                return mid
            elif mat[mid][0] > t:
                return rowSearch(mat, t, lo, mid - 1)
            else: # mat[mid][-1] < t # implicit
                return rowSearch(mat, t, mid + 1, hi)

        r_idx = rowSearch(matrix, target, 0, len(matrix))
        return binarySearch(matrix[r_idx], target, 0, len(matrix[r_idx]))

        