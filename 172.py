from math import factorial

class Solution:
    def trailingZeroes(self, n: int) -> int:
        f = factorial(n)
        count = 0 
        for num in str(f)[::-1]:
            if int(num) == 0:
                count += 1
            else:
                break
        return count
s = Solution()
print(s.trailingZeroes(3))