from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] = counts.get(num) + 1
            else:
                counts[num] = 1
        r = []
        for count in counts:
            if counts[count] == 1:
                r.append(count)
        return r
    def singleNumberSpace(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        while len(nums) > i+1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                nums.pop(i)
            else:
                i += 1
        return nums

s = Solution()
print(s.singleNumberSpace([1,2,1,3,2,5]))
