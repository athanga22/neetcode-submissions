class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1])
        v1=nums[0]
        v2=max(nums[0], nums[1])
        for i in range(2, n):
            temp=max(v2, nums[i]+v1)
            v1=v2
            v2=temp
        return v2