from typing import List
# DFS 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        if grid == []:
            return 0
        num = 0
        y_len = len(grid)
        x_len = len(grid[0])
        for i in range(x_len):
            for j in range(y_len):
                if int(grid[j][i]) == 1:
                    num += 1
                    self.processIsland(grid, i, j, x_len, y_len)

        return num

    def processIsland(self, grid: List[List[str]], x: int, y: int, x_len: int, y_len: int):
        if x < 0 or x > x_len-1 or y < 0 or y > y_len-1:
            return
        elif int(grid[y][x]) == 1:
            grid[y][x] = "2"
            self.processIsland(grid, x-1, y, x_len, y_len)
            self.processIsland(grid, x+1, y, x_len, y_len)
            self.processIsland(grid, x, y-1, x_len, y_len)
            self.processIsland(grid, x, y+1, x_len, y_len)
        return