from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        l = len(grid)
        w = len(grid[0])
        m = 0
        mainqueue = []
        for i in range(w):
            for j in range(l):
                if grid[i][j] == 1:
                    mainqueue.append((i+1,j))
                    mainqueue.append((i-1,j))
                    mainqueue.append((i,j+1))
                    mainqueue.append((i,j-1))
        count = 1
        subqueue = []
        while mainqueue:
            count += 1
            while mainqueue:
                p = mainqueue.pop(0)
                if p[0] >= 0 and p[1] >= 0 and p[0] < w and p[1] < l and grid[p[0]][p[1]] == 0:
                    grid[p[0]][p[1]] = count     
                    subqueue.append((p[0]+1,p[1]))
                    subqueue.append((p[0]-1,p[1]))
                    subqueue.append((p[0], p[1]+1))
                    subqueue.append((p[0],p[1]-1))
            mainqueue = subqueue.copy()
            subqueue = []
        if count == 2:
            return -1
        return count-2

        


s = Solution()
grid = [[1,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))
'''   
        l = len(grid)
        w = len(grid[0])
        m = 0
        for i in range(w):
            for j in range(l):
                if(grid[i][j] == 0):
                    test_m = self.dfs(grid,i,j,w-1,l-1)
                    m = max(test_m, m)
        return m

    def dfs(self, grid, x, y, x_max, y_max):
        if x > x_max or y > y_max:
            return 0
        if grid[x][y] == 0:
            m1 = self.dfs(grid,x+1,y, x_max, y_max) + 1
            m2 = self.dfs(grid,x-1,y, x_max, y_max) + 1
            m3 = self.dfs(grid,x,y-1, x_max, y_max) + 1
            m4 = self.dfs(grid,x,y+1, x_max, y_max) + 1
            return max(m1,m2,m3,m4)
        else:
            return 0

s = Solution()
grid = [[1,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))
'''