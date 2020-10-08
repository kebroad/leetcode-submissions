class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        l = [a for a in range(n+1)]
        l[1] = 1
        l[2] = 2
        for i in range(3,n+1):
            l[i] = l[i-1] + l[i-2]
        return l[n]

s = Solution()
print(s.climbStairs(100))