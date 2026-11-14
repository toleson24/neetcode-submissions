class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        
        i = 0   
        j = 0

        g.sort()
        s.sort()

        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                count += 1
                j += 1
            
            i += 1

        return count

        