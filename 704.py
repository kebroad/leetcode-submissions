from typing import List

#TODO
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        while high >= low:







    #     return self.searchIn(nums, 0, len(nums)-1, target)

    # def searchIn(self, nums: List[int], low: int, high: int, target: int):
    #     mid = (high - low) // 2
    #     if nums[mid] == target:
    #         return mid
    #     elif target < nums[mid] :
    #         return self.searchIn(nums, low, mid-1, target)
    #     elif target > nums[mid]:
    #         return self.searchIn(nums, mid+1, high, target)
    #     return -1

s = Solution()

#print(s.search([-1,0,3,5,9,12], 2))
print(s.search([-1,0,3,5,9,12], 9))
