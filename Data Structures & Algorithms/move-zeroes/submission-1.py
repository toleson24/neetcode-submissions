class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0 for _ in range(len(nums))]
        
        i = 0
        for n in nums:
            if n != 0:
                arr[i] = n
                i += 1

        for i in range(len(arr)):
            nums[i] = arr[i]

        return nums

        