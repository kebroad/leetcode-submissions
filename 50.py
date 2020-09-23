class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = abs(n)
        res = x
        if p== 0:
            return 1
        if p%2 == 0:
            res = self.myPow(x*x, p//2)
        else:
            res = x * self.myPow(x*x,p//2)
        if n < 0:
            res = 1/res
        return res
    
s = Solution()
print(s.myPow(2.00000,-2))