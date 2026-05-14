class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        v1 = nums[0]
        v2 = max(nums[0], nums[1])
        for i in range(2, n-1):
            temp = max(v2, nums[i] + v1)
            v1 = v2
            v2 = temp
        v3 = nums[1]
        v4 = max(nums[1], nums[2])
        for i in range(3, n):
            temp = max(v4, nums[i] + v3)
            v3 = v4
            v4 = temp
        return max(v2, v4)