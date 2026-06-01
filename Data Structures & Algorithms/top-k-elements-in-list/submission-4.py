from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = Counter(nums)
        freqmap = defaultdict(list)
        for key in d:
            freqmap[d[key]].append(key)

        res = []
        for f in range(n, 0, -1):
            if f in freqmap:
                for i in freqmap[f]:
                    res.append(i)
                    if len(res) == k:
                        return res
        return res
