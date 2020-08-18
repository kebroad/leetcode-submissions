import math
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0]*len(T)
        tempStack = []
        for i, temp in enumerate(T):
            while tempStack and temp > tempStack[-1][0]:
                oldTemp,oldTempIndex = tempStack.pop()
                result[oldTempIndex] = i-oldTempIndex 
            tempStack.append([temp, i])
        return result

T = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
print(s.dailyTemperatures(T))