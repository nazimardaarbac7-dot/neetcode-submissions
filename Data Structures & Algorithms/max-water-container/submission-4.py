class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        left = 0
        right = n-1
        best = 0
        while left < right:
            leftH = heights[left]
            rightH = heights[right]
            h = min(leftH,rightH)
            z = right - left
            area = h * z 
            best = max(area,best)
            if leftH < rightH:
                left +=1
            else :
                right -= 1
        return best