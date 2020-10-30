class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0
        g = [[0 for _ in range(n)] for _ in range(n)]
        for dif in range(0, n):
            for i in range(0, n-dif):
                j = i + dif
                if dif == 0:
                    g[i][j] = 1
                    c += 1
                elif (dif == 1) and (s[i] == s[j]):
                    g[i][j] = 1
                    c += 1                   
                elif (s[i] == s[j]) and (g[i+1][j-1] == 1):
                    g[i][j] = 1
                    c += 1
        return c

s = Solution()
print(s.countSubstrings("aaa"))