class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return 1
        lens=[1]*(n)
        mx=0
        for i in range(1, n):
            for j in range(0, i):
                if nums[j]<nums[i]:
                    lens[i]=max(lens[j]+1,lens[i])
            mx=max(lens[i], mx)
        return mx