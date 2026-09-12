class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, e=0, 0
        n=len(s)
        char_set=set()
        mx=0

        while e<n:
            while s[e] in char_set:
                char_set.remove(s[st])
                st+=1
            
            char_set.add(s[e])
            mx=max(mx, e-st+1)
            e+=1
        
        return mx