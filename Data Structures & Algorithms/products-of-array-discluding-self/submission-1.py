class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        suf=[1]*n
        
        pre[0]=nums[0]
        suf[n-1]=nums[n-1]
        for i in range(1, n):
            pre[i]=pre[i-1]*nums[i]
        for i in range(n-2, -1, -1):
            suf[i]=suf[i+1]*nums[i]
        
        res=[1]*n
        for i in range(n):
            if i-1>=0: res[i]*=pre[i-1]
            if i+1<n: res[i]*=suf[i+1]
        
        return res

