class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        carr = [0] * 26
        for c in s:
            carr[ord(c) - ord("a")] += 1
        for c in t:
            carr[ord(c) - ord("a")] -= 1

        for c in carr:
            if c != 0:
                return False

        return True
