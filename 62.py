class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        grid[0][0] = 1
        for v in range(1,m+n):
            for i in range(0,v+1):
                j = v - i
                if (i < n) and (j < m):
                    if i-1 >= 0:
                        grid[i][j] += grid[i-1][j]
                    if j-1 >= 0:
                        grid[i][j] += grid[i][j-1]         
        return grid[n-1][m-1]              
s = Solution()
print(s.uniquePaths(4,4))

print(max(2,2))