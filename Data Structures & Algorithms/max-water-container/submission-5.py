class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        mostArea = 0
        while left<right:
            h = min(heights[left],heights[right])
            m = right - left
            area = h * m
            mostArea = max(mostArea,area)
            if heights[left] < heights[right]:
                 left+=1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left+=1
                right-=1
        return mostArea