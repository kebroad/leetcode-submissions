class Solution:
    def climbStairs(self, n: int) -> int:
        return 1 + n-1 + n-2


s = Solution()
print(s.climbStairs(3))