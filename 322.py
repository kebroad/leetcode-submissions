from typing import List

class Solution:
    def __init__(self):
        self.cache = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        count = 0
        amounts = set()
        amounts.add(amount)
        while amounts and 0 not in amounts:
            count += 1
            temp = set()
            for coin in coins:
                for a in amounts:
                    if a-coin >= 0:
                        temp.add(a-coin)
            amounts = temp
        if not amounts:
            return -1
        return count



    #     res = self.coinChangeRecur(coins, amount, 0)
    #     if res == 1000000000:
    #         return -1
    #     else:
    #         return res
    
    
    # def coinChangeRecur(self, coins: List[int], amount: int, count) -> int:
    #     if (amount,count) in self.cache:
    #         print("cache hit")
    #         return self.cache[(amount,count)]
    #     if amount == 0:
    #         return count
    #     l = []
    #     for coin in coins:
    #         if amount - coin >= 0:
    #             l.append(self.coinChangeRecur(coins,amount-coin,count + 1))
    #     if not l:
    #         return 1000000000
    #     r = min(l)
    #     self.cache[(amount,count)] = r
    #     return r

s = Solution()
print(s.coinChange([1,2,5],11))