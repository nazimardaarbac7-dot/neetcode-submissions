class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most =  0
        left_pointer = 0
        right_pointer=len(heights)-1
        while(left_pointer<right_pointer):
            left_bar = heights[left_pointer]
            right_bar = heights[right_pointer]

            current_water = (right_pointer-left_pointer)*min(left_bar,right_bar)

            if left_bar < right_bar:
                left_pointer+=1
            else:
                right_pointer-=1

            most = max(current_water,most)
        return most


        