import math

class Solution:
    def countPrimes(self, n: int) -> int:
        #https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        count =  [1] * n
        if (n is 0) or (n is 1):
            return 0
        else:
            count[0] = 0
            count[1] = 0
        for i in range(2, int(math.sqrt(n))+1):
                for j in range(i**2, n, i):
                    count[j] = 0
        return sum(count)

s = Solution()
print(s.countPrimes(10))