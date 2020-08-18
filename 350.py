from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1c = {}
        nums2c = {}
        for num in nums1:
            if num in nums1c:
                nums1c[num] = nums1c[num] + 1                
            else:
                nums1c[num] = 1

        for num in nums2:
            if num in nums2c:
                nums2c[num] = nums2c[num] + 1                
            else:
                nums2c[num] = 1
        final = []

        for num in nums1c:
            if num in nums2c:
                for index in range(min(nums1c[num], nums2c[num])):
                    final.append(num)
        return final

        
s = Solution()
print(s.intersect([1,2,2,1], [2,2]))
