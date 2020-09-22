class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = bin(n)[2:]
        leftover = (32 - len(reversed))
        reversed = reversed
        res = 0
        for i, bit in enumerate(reversed):
            res += (2 ** i)* int(bit)
        res = res << leftover
        return res

s = Solution()
print(s.reverseBits(43))