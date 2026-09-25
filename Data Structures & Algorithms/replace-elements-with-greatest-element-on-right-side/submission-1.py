class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            largest = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > largest:
                    largest = arr[j]
            arr[i] = largest
        return arr

        