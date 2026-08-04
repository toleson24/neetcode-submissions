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

                r_min = mat[mid][0]
                r_max = mat[mid][-1]

                if r_min <= t <= r_max:
                    return mid
                elif r_min > t:
                    hi = mid - 1
                else: # r_max < t
                    lo = mid + 1
                
            return -1

        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        r_idx = rowSearch(matrix, target, 0, len(matrix) - 1)
        return binarySearch(matrix[r_idx], target, 0, len(matrix[r_idx]) - 1)

        