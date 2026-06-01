class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        lmx, rmx = height[l], height[r]
        total = 0
        while l < r:
            if lmx < rmx:
                l += 1
                lmx = max(lmx, height[l])
                total += lmx - height[l]
            else:
                r -= 1
                rmx = max(rmx, height[r])
                total += rmx - height[r]

        return total
