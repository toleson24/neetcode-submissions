class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # odd
            beg = i
            end = i
            while 0 <= beg and end < len(s) and s[beg] == s[end]:
                count += 1
                beg -= 1
                end += 1
            
            # even
            beg = i
            end = i + 1
            while 0 <= beg and end < len(s) and s[beg] == s[end]:
                count += 1
                beg -= 1
                end += 1

        return count
        