import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        a = 1
        while a <= n:
            a = 3 ** i
            if a == n:
                return True
            i += 1
        return False
s = Solution()
print(s.isPowerOfThree(1))

