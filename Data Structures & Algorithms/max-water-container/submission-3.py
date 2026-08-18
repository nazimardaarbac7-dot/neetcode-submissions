class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0 
        j = n-1
        best = 0
        while i != j:
            width = abs(i-j)
            height = min(heights[i],heights[j])
            area = width * height
            best = max(area,best)
            if heights[i] > heights[j]:
                j -=1 
            else : 
                i+= 1
        return best
