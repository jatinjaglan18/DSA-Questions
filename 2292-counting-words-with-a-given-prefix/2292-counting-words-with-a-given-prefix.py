class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        p = len(pref)
        count = 0
        for w in words:
            if len(w) >= p and w[:p] == pref:
                count += 1
        return count
