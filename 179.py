from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                cur_result = "".join([str(nums[i]), str(nums[j])])
                new_result = "".join([str(nums[j]), str(nums[i])])
                if int(new_result) > int(cur_result):
                    nums[i], nums[j] = nums[j], nums[i]
        for num in nums:
            res.append(str(num))
        return "".join(res)

s = Solution()
print(s.largestNumber([10,2]))
