class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        count = 0
        for d in b:
            if d == '1':
                count += 1
        return count


s = Solution()
print(s.hammingWeight(1))