from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        rm = nums[0]
        for i in range(1,len(nums)):
            m = max(nums[i], m + nums[i])
            rm = max(m, rm)
        return rm

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))