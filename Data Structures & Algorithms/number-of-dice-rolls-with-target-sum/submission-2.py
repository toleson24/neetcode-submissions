class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n:
            return 0
        if target > n * k:
            return 0

        def count_combos(a: int, b: int) -> int:
            return int(math.factorial(a) // (math.factorial(b) * math.factorial(a - b)))

        count = 0
        for j in range(int((target - n) // k) + 1):
            count += ((-1) ** j) * count_combos(n, j) * count_combos(target - 1 - j * k, n - 1)
        
        return count % 1000000007
        
