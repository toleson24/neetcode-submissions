import copy

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # ans = [0 for _ in range(len(arr))]
        # ans = list(arr)
        # ans = [0] * len(arr)
        # ans = arr.copy()
        ans = copy.deepcopy(arr)
        largest = -1
        for i in range(len(arr) - 1, -1, -1):
            ans[i] = largest  
            largest = max(arr[i], largest)
        return ans

        