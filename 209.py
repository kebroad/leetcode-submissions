from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] >= s:
                return 1
            else:
                return 0
        if nums[0] >= s:
            return 1
        run_max = nums[0]
        min_length = 1000000000
        start_index = 0
        for index in range(1,len(nums)):
            if run_max+nums[index] > run_max:
                run_max = run_max+nums[index]
            else:
                run_max = nums[index]
                start_index = index
            if run_max >= s:
                res = run_max
                better_index  = start_index
                while res-nums[better_index] >= s:
                    better_index += 1
                    res = res - nums[better_index]
                if min_length >index-better_index+1:
                    min_length = index-better_index+1
                start_index = better_index
                run_max = res
        if min_length == 1000000000:
            return 0
        else:
            return min_length


l2 = [10,2,3]
#l = [2,3,1,2,4,3]
s = Solution()
print(s.minSubArrayLen(6,l2))
#print(s.minSubArrayLen(11,l2))