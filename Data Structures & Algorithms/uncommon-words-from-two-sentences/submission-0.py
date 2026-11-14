class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        seen = set()
        dupes = set()

        for w in (s1 + " " + s2).split():
            if w in seen:
                dupes.add(w)
            else:
                seen.add(w)

        return list(seen - dupes)