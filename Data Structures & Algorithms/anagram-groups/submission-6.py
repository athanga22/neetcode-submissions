class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def strHash(s):
            carr = [0] * 26
            for c in s:
                carr[ord(c) - ord("a")] += 1
            return carr

        d = defaultdict(list)
        for s in strs:
            d[tuple(strHash(s))].append(s)

        return list(d.values())
