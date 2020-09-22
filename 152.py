from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxPrefix = [0] * len(nums)
        minPrefix = [0] * len(nums)
        for i, num in enumerate(nums):
            maxPrefix[i] = max(num, maxPrefix[i-1]* num, minPrefix[i-1]*num)
            minPrefix[i] = min(num, maxPrefix[i-1]* num, minPrefix[i-1]*num)
        return max(maxPrefix)


s = Solution()
print(s.maxProduct([1]))