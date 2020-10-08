from typing import List

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n for n in range(0,n+1)]
        for i in range(len(dp)):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], 1+dp[i-j*j])
                j += 1
        return dp[n]

    #     if n == 1:
    #         return 1
    #     if n == 0:
    #         return 0
    #     square_list = []
    #     i = 1
    #     while i**2 <= n:
    #         square_list.append(i**2)
    #         i += 1
    #     l = self.numSquaresRecur(n, 0, square_list)
    #     return min(l)
        
    # def numSquaresRecur(self, n: int, count: int, squares: List[int]):
    #     l = []
    #     for num in squares[::-1]:
    #         if num == n:
    #             return [count + 1]
    #         if num < n:
    #             l.extend(self.numSquaresRecur(n-num, count + 1, squares))
    #     return l


s = Solution()
print(s.numSquares(4))
