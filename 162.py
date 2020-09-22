from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.findPeakElementRecurring(nums, 0, len(nums) - 1)

    def findPeakElementRecurring(self, nums: List[int], low: int, high: int) -> int:
        if high-low < 2:
            if (low == 0) and (nums[low] > nums[high]):
                return low
            if (high == len(nums) - 1) and (nums[high] > nums[low]):
                return high
            return 0
        mid = ((high-low) // 2) + low
        if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
            return mid
        lowside = self.findPeakElementRecurring(nums, low, mid)
        if lowside > 0:
            return lowside
        highside = self.findPeakElementRecurring(nums, mid, high)
        if highside > 0:
            return highside
        return 0
    

s = Solution()
print(s.findPeakElement([1,2,3,4,5]))