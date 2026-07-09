class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        letters = {}
        for i, ch in enumerate(s):
            if ch in letters:
                ans = max(ans, i - letters[ch] - 1)
            else:
                letters[ch] = i

        return ans 

        