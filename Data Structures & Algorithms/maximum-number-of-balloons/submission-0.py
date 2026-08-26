from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        counts = Counter(text)

        instances = len(text)
        for ch in balloon:
            instances = min(instances, counts[ch] // balloon[ch])
        
        return instances
        