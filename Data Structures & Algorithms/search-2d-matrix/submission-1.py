class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(r, t, lo, hi):
            if lo > hi:
                return False 
            
            mid = lo + (hi - lo) // 2

            if r[mid] == t:
                return True
            elif r[mid] < t:
                return binarySearch(r, t, mid + 1, hi)
            else: # r[mid] > t
                return binarySearch(r, t, lo, mid - 1)
            
            return False

        def rowSearch(m, t, lo, hi):
            if lo > hi:
                return -1
            
            mid = lo + (hi - lo) // 2

            r_min = m[mid][0]
            r_max = m[mid][-1]

            if r_min <= t <= r_max:
                return mid
            elif r_min > t:
                return rowSearch(m, t, lo, mid - 1)
            else: # r_max < t:
                return rowSearch(m, t, mid + 1, hi)

        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        r_idx = rowSearch(matrix, target, 0, len(matrix))
        return binarySearch(matrix[r_idx], target, 0, len(matrix[r_idx]))

        