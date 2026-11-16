class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {}
        l = 0
        length = 0

        for r in range(len(s)):
            if s[r] in indices:
                l = max(l, indices[s[r]] + 1)
            
            indices[s[r]] = r
            length = max(length, r - l + 1)
        
        return length

        