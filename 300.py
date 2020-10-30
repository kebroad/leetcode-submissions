from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        a = [1]* len(nums)
        for j in range(len(nums)):
            i = 0
            while i < j:
                if nums[j] > nums[i]:
                    a[j] = max(a[i] + 1, a[j])
                i += 1
        return max(a)

s = Solution()
print(s.lengthOfLIS([10]))