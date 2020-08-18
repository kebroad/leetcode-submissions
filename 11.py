from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i != j:
                    dist = abs(i-j)
                    area = min(height[i],height[j])* dist
                    if(area > max):
                        max = area               
        return max

s = Solution()

print(s.maxArea([1,1]))