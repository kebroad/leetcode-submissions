from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, num in enumerate(nums):
            if i > m:
                return False
            if i + num > m:
                m = i+num
        return True








        # max_reach = 0
        # if nums[0] == 0:
        #     return False   
        # for i,num in enumerate(nums):
        #     if i > max_reach:
        #         return False
        #     if (i + num) > max_reach:
        #         max_reach = i + num
        # return True
        

s = Solution()
print(s.canJump([1,1,2,3,2,1,0,0,1,3]))
    