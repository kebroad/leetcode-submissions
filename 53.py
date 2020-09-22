from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        run_sum = nums[0]
        for num in nums[1:]:
            run_sum = max(num, run_sum + num)
            if run_sum > cur_max:
                cur_max = run_sum
        return cur_max

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))