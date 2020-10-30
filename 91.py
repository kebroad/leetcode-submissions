class Solution:
    def numDecodings(self, s: str) -> int:
        return self.numDecodingsR(s, 0, len(s))

    def numDecodingsR(self, s: str, index: int, n: int):
        if index > n-1:
            return 1
        f= 0
        if (index <= n-2) and (0 < ((int(s[index]) *10) + int(s[index+1])) <= 26):
            f += self.numDecodingsR(s, index + 2, n)
        if int(s[index]) > 0:
            f += self.numDecodingsR(s, index + 1, n)
        return f

        # if s == "0":
        #     return 0
        # n = len(s)
        # if n == 1:
        #     return  1
        # arr = [0] * n
        # if int(s[0]) > 0:
        #     arr[0] = 1
        # else:
        #     arr[0] = 0
        # if (int(s[0]) != 0) and (((int(s[0]) *10) + int(s[1])) <= 26):
        #     arr[1] = 2
        # elif int(s[1]) > 0:
        #     arr[1] = 1
        # else: arr[1] = 0
        # for i in range(2,n):
        #     val = 0
        #     if int(s[i]) > 0:
        #         val += 1
        #     if ((int(s[i-1]) *10) + int(s[i])) <= 26:
        #         val += 1
        #     arr[i] = max(val+arr[i-2], 1+arr[i-1])
        # return arr[n-1]

s = Solution()
print(s.numDecodings("226"))