from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        s = 0

        for word in words:
            l = len(word)
            add = True
            w_fd = {}
            for ch in word:
                if ch not in c:
                    add = False
                    break
                
                w_fd[ch] = w_fd.get(ch, 0) + 1
                if w_fd[ch] > c[ch]:
                    add = False
                    break
                
            if add:
                s += l

        return s

        