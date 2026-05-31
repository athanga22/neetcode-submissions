class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = defaultdict(int)
        freqmap = defaultdict(list)
        res = []
        for i in nums:
            d[i] += 1

        for key in d:
            freqmap[d[key]].append(key)

        for f in range(n, 0, -1):
            if f in freqmap:
                for i in freqmap[f]:
                    res.append(i)
                    if len(res) == k:
                        return res
        
        return res
