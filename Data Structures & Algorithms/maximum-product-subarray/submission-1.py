class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        mx = mn = nums[0]
        max_pro = mx
        for i in range(1, n):
            cands = (nums[i], nums[i] * mx, nums[i] * mn)
            mx = max(cands)
            mn = min(cands)
            max_pro = max(max_pro, mx)

        return max_pro
