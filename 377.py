from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        a = [0]* (target+1)
        a[0] = 1
        for i in range(1,len(a)):
            for num in nums:
                if num <= i:
                    a[i] += a[i-num]
        return a[target]

s = Solution()
print(s.combinationSum4([1, 2, 3], 4))