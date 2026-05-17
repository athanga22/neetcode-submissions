class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        words=set(wordDict)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1, n+1):
            for word in words:
                if i-len(word)>=0 and dp[i-len(word)] and s[i-len(word):i] in words:
                    dp[i]=dp[i-len(word)]
                    break
            
        return dp[n]