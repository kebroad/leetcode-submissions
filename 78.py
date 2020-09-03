from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rlist = [[]]
        if nums is None:
            return rlist 
        for num in nums:
            for rindex in range(len(rlist)):
                sub = (rlist[rindex]) +[num]
                rlist.append(sub)
        return rlist

s = Solution()
print(s.subsets([1,2,3]))