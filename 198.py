from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None:
            return None
        suml1 = [n for i, n in enumerate(nums) if i % 2 == 0]
        sum1 = sum(suml1)
        suml2 = [n for i, n in enumerate(nums) if i % 2 == 1]
        sum2 = sum(suml2)
        return max(sum1, sum2)

s = Solution()
print(s.rob([1,2,3,1]))