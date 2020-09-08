class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        curr = n
        while 1:
            digits = [int(dig) for dig in str(curr)]
            sum = 0
            for digit in digits:
                sum += (digit ** 2)
            if sum == 1:
                return True
            elif sum in s:
                return False
            else:
                s.add(sum)
                curr = sum
        

            
n="12345"
digits = [int(dig) for dig in str(n)]
