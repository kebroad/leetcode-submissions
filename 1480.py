from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumNums = []
        for i in range(len(nums)):
            sumNum = 0
            for j in range(i+1):
                sumNum += nums[j]
            sumNums.append(sumNum)
        return sumNums

s = Solution()
print(s.runningSum([1,2,3,4]))