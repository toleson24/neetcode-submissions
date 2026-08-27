def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sortState = []

        i = 0
        while i < len(pairs):
            j = i
            while j > 0 and pairs[j - 1].key > pairs[j].key:
                swap(pairs, j, j - 1)
                j -= 1
            sortState.append(pairs[:])
            i += 1
        
        return sortState
        
    def bubbleSort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    swap(arr[i], arr[j])
        
        return arr
    
    def selectionSort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] < arr[i]:
                    swap(arr[i], arr[j])

        return arr