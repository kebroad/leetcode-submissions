from typing import List
from collections import Counter 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        for num in range(len(nums)+1):
            if numsCount[num] == 0:
                return num

s = Solution()
print(s.missingNumber([3,0,1]))