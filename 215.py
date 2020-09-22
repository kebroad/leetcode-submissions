from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))