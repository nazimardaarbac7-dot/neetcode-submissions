class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplet_set = set()

        for first_index in range(len(sorted_nums)-2):
            first_number = sorted_nums[first_index]
            if first_number > 0 :
                break
            left_index = first_index +1 
            right_index = len(sorted_nums)-1
            while(left_index<right_index):
                current_sum = sorted_nums[left_index] + first_number + sorted_nums[right_index]

                if current_sum == 0:
                    triplet_set.add(tuple(sorted([first_number,sorted_nums[left_index],sorted_nums[right_index]])))
                    left_index +=1
                    right_index -= 1
                elif current_sum <0:
                    left_index+=1
                else:
                    right_index-=1
        result =[]
        for triplet in triplet_set:
            trip_list = list(triplet)
            result.append(triplet)
        return result




