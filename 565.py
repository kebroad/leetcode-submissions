from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        m = 0
        visited = set()
        for i in range(len(nums)):
            if i in visited:
                continue
            s = set()
            index = i
            count = 0
            while index not in s:
                visited.add(index)
                s.add(index)
                index = nums[index]
                count += 1
            if len(s) > m:
                m = len(s)
        return m