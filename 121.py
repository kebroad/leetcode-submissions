from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        arr = [0]* len(prices)
        m = prices[0]
        arr = 0
        for i in range(1,n):
            arr = max(arr, prices[i] - m)
            m = min(m, prices[i])
        return arr

s  = Solution()
print(s.maxProfit([7]))