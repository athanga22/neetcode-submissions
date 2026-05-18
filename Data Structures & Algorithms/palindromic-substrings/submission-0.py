class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        cnt = 0
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n:
                    break
                if i == j:
                    dp[i][j] = True
                elif j - i + 1 == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j]:
                    cnt += 1
        return cnt
