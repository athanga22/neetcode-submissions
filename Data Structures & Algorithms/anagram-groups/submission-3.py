class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def strHash(s):
            carr = [0] * 26
            for c in s:
                carr[ord(c) - ord("a")] += 1
            return carr

        d = {}
        for s in strs:
            s_hash = str(strHash(s))
            if s_hash not in d:
                d[s_hash] = []
                d[s_hash].append(s)
            else:
                d[s_hash].append(s)

        res = []
        for h in d:
            res.append(d[h])

        return res
