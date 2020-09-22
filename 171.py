class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0 
        n = len(s)
        for i, char in enumerate(s):
            p = (n-(i+1))
            power = 26 ** p
            num += (ord(char)-64) * power
        return num

s = Solution()
print(s.titleToNumber("AA"))


#print(ord('Y')-64)