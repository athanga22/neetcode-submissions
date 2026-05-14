class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n==2: return cost[0]

        c1, c2=cost[0], cost[1]

        for i in range(2, n):
            temp=min(c1, c2)+cost[i]
            c1=c2
            c2=temp
        
        return min(c1, c2)