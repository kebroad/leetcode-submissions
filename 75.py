from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums)
        mid = 1
        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        k -= 1
        j-= 1
        while j >= i:
            if nums[j] > 1:
                nums[j],nums[k] = nums[k], nums[j]
                k-= 1
            j -= 1

s = Solution()
l = [2,0,2,1,1,0]
s.sortColors(l)
print(l)