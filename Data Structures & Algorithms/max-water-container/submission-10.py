class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0 
        right = n-1 
        best = 0
        while left < right:
            h = min(heights[left],heights[right])
            m = right - left 
            area = h * m 
            best = max(best , area)
            if heights[left] < heights[right]:
                left+= 1
            else:
                right -= 1
        return best