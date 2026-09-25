class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        k = 0
        for c in s:
            if k < len(t) and t[k] == c:
                k += 1

        return len(t) - k