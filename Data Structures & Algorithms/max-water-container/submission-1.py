class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        max_container = float("-inf")
        
        while i < j:
            max_container = max(max_container, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_container
