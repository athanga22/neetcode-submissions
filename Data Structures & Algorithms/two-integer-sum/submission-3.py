class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        res=[]
        for i in range(n):
            half=target-nums[i]
            if half in d:
                res=[d[half], i]
                break
            else:
                d[nums[i]]=i
        
        return res