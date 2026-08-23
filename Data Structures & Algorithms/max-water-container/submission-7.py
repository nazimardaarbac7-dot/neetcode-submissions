class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0 
        most = 0
        right = n-1
        while left < right:
            h = min(heights[left],heights[right])
            m = right- left
            area = h * m 
            if most < area:
                most = area
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return most
            