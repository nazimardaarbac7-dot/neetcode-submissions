class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        best = 0
        right = len(heights) - 1
        while left < right:
            h = min(heights[left],heights[right])
            m = right - left 
            area = h * m 
            best = max(area,best)
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1 
        return best
