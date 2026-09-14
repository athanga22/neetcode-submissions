class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r=1, max(piles)
        while l<=r:
            totalTime=0
            mid_rate=(l+r)//2
            for p in piles:
                totalTime+=math.ceil(p/mid_rate)
            
            if totalTime<=h:
                rate=mid_rate
                r=mid_rate-1
            else:
                l=mid_rate+1
        
        return rate
