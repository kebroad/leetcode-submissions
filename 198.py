from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        elif n == 0:
            return 0
        arr = [0]* (n+1)
        arr[0] = 0
        arr[1] = nums[0]
        for i in range(2,n+1):
            arr[i] = max(arr[i-2] + nums[i-1], arr[i-1])
        return arr[n]
s = Solution()
print(s.rob([2,7,9,3,1]))