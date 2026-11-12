class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = [None for _ in range(len(nums1) + len(nums2))]
        p1 = 0
        p2 = 0
        i = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1][0] < nums2[p2][0]:
                result[i] = nums1[p1]
                p1 += 1
            elif nums1[p1][0] == nums2[p2][0]:
                result[i] = [nums1[p1][0], nums1[p1][1] + nums2[p2][1]]
                p1 += 1
                p2 += 1
            else: # nums1[p1][0] > nums2[p2][0]:
                result[i] = nums2[p2]
                p2 += 1

            i += 1

        while p1 < len(nums1):
            result[i] = nums1[p1]
            p1 += 1
            i += 1

        while p2 < len(nums2):
            result[i] = nums2[p2]
            p2 += 1
            i += 1

        return [l for l in result if l]
