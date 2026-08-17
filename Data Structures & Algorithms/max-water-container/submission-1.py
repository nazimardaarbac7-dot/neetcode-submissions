class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0 
        n = len(heights)
        left = 0
        right = n-1
        while left < right:
            leftHeight = heights[left]
            rightHeight = heights[right]
            minHeight = min(leftHeight,rightHeight)
            base = right - left
            container = base * minHeight
            most = max(container,most)
            if leftHeight < rightHeight:
                left += 1 
            else:
                right -= 1 
            
        return most


        