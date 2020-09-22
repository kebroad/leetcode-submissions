from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = {}
        for num in nums:
            if num in c:
                c[num] = c.get(num) + 1
            else:
                c[num] = 1
        return(any(c[k] >= 2 for k in c))


s = Solution()
print(s.containsDuplicate([1,2,3]))