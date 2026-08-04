class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row: List[int], t: int, lo: int, hi: int) -> bool: 
            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if row[mid] == t:
                    return True
                elif row[mid] > t:
                    hi = mid - 1
                else: # row[mid] < t
                    lo = mid + 1
                
            return False

        def rowSearch(mat: List[List[int]], t: int, lo: int, hi: int) -> bool:
            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if mat[mid][0] <= t <= mat[mid][-1]:
                    return mid
                elif mat[mid][0] > t:
                    hi = mid - 1
                else: # mat[mid][-1] < t
                    lo = mid + 1
                
            return -1

        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        r_idx = rowSearch(matrix, target, 0, len(matrix) - 1)
        return binarySearch(matrix[r_idx], target, 0, len(matrix[r_idx]) - 1)

        