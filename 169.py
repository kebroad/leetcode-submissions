from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        d = {}
        m = 0
        m_i = -1 
        for num in nums:
            if num not in  d:
                d[num] = 1
            else:
                d[num] = d.get(num) + 1
            if d[num] > m:
                m = d[num]
                m_i = num
        if d[m_i] > (len(nums) // 2):
            return m_i
        else:
            return -1
        
s = Solution()
print(s.majorityElement([1]))