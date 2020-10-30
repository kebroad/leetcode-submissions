
class Solution:
    def __init__(self):
        self.cache = {}
    def findTargetSumWays(self, nums: list, S: int) -> int:
        n = len(nums)
        if not nums:
            return (S == 0)
        if (n, S) in self.cache:
            return self.cache[(n, S)]

        num = nums.pop(0)
        count = 0   
        count += self.findTargetSumWays(nums.copy(), S-num)
        count += self.findTargetSumWays(nums.copy(), S+num)
        self.cache[(n, S)] = count
        return count

    # def findTargetSumWaysRecur(self, nums: List[int], S: int) -> int:
    #     if len(nums) == 1:
    #         return (S == 0)
    #     num = nums.pop(0)
    #     count += self.findTargetSumWaysRecur(nums, S-num)
    #     count += self.findTargetSumWaysRecur(nums, S+num)
    #     return count

s = Solution()
print(s.findTargetSumWays([0,0,1], 1))

print(str([1,2,3,4]))