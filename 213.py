from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[1]
        if len(nums) == 2:
            return 0
        if len(nums) == 1:
            return a[0]
        nums1 = nums.copy()
        nums2 = nums.copy()
        nums1.pop(len(nums1)-1)
        nums2.pop(0)
        a1 = [0] * len(nums1)
        a1[0] = nums1[0]
        a1[1] = nums1[1]
        for i in range(1,len(nums1)):
            a1[i] = max(a1[i-1], nums1[i] + a1[i-2])
        a2 = [0] * len(nums2)
        a2[0] = nums2[0]
        a2[1] = nums2[1]
        for i in range(1,len(nums2)):
            a2[i] = max(a2[i-1], nums2[i] + a2[i-2])
        return max(a1[len(nums1)-1],a2[len(nums2)-1])

s = Solution()
print(s.rob([1,2,3,1]))