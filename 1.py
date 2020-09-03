from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            d[target-num] = index
        for index, num in enumerate(nums):
            if((num in d) and (d[num] != index)):
                return [index, d[num]]
        return [-1,-1]

s = Solution()
print(s.twoSum([3,2,4], 6))