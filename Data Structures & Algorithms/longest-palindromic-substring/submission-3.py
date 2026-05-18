class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        st, e = 0, 0

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(n):
            l, r = expand(i, i)
            if r - l > e - st:
                st, e = l, r

            l, r = expand(i, i + 1)
            if r - l > e - st:
                st, e = l, r

        return s[st : e + 1]
