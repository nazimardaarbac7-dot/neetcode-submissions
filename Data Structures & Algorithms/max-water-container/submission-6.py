class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        m = -1
        left = 0
        right = n-1
        while left<right:
            h = min(heights[left], heights[right])
            f = right - left
            a = h * f
            m = max(m,a)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return m




            