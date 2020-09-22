class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ''
        neg = False
        if(num < 0):
            num *= -1
            neg = True
        while num != 0:
            s = str(num % 7) + s
            num = num // 7
        if neg == True:
            s = '-' + s
        return int(s)
s = Solution()
print(s.convertToBase7(-100))