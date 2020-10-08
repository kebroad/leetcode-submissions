from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        n = len(nums)
        count = 0
        found = True
        while found:
            found = False
            for i in range(1,n-1):
                if nums[i-1] < nums[i] > nums[i+1]:
                    found = True
                    count += nums[i]
                    nums[i-1], nums[i], nums[i+1] = 0,0,0

        if nums[0] or nums[n-1]:
            if nums[n-1] < nums[0] > nums[1]:
                count += nums[0]
                nums[n-1],nums[0],nums[1] = 0,0,0
            elif nums[0] < nums[n-1] > nums[n-2]:
                count += nums[n-1]
                nums[n-1],nums[0],nums[1] = 0,0,0

        for i in range(1,n-1):
            if nums[i] != 0:
                count += nums[i]
                nums[i-1], nums[i], nums[i+1] = 0,0,0

        if nums[0] or nums[n-1]:
            count += max(nums[0], nums[n-1])
        return count


s = Solution()
print(s.rob([1,1,1]))