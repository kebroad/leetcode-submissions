from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        y_len = len(board)
        x_len = len(board[0])
        board_ones = []
        for x in range(x_len):
            for y in range(y_len):
                ones = self.neighboringOnes(board,x,y,x_len,y_len)
                if (ones >= 2) and (ones <= 3) and (board[y][x]):
                    board_ones.append((x,y))
                if (ones == 3) and (not board[y][x]):
                    board_ones.append((x,y))
        for x in range(x_len):
            for y in range(y_len):
                if (x,y) in board_ones:
                    board[y][x] = 1
                else:
                    board[y][x] = 0
        print(board)


    def neighboringOnes(self, board: List[List[int]], x,y, x_len, y_len):
        count = 0
        if (x+1 < x_len) and (x+1 >= 0):
            count += board[y][x+1]
        if (x-1 < x_len) and (x-1 >= 0):
            count += board[y][x-1]
        if (y-1 < y_len) and (y-1 >= 0):
            count += board[y-1][x]
        if (y+1 < y_len) and (y+1 >= 0):
            count += board[y+1][x]
        if (x+1 < x_len) and (x+1 >= 0) and (y+1 < y_len) and (y+1 >= 0):
            count += board[y+1][x+1]
        if (x+1 < x_len) and (x+1 >= 0) and (y-1 < y_len) and (y-1 >= 0):
            count += board[y-1][x+1]
        if (x-1 < x_len) and (x-1 >= 0) and (y+1 < y_len) and (y+1 >= 0):
            count += board[y+1][x-1]
        if (x-1 < x_len) and (x-1 >= 0) and (y-1 < y_len) and (y-1 >= 0):
            count += board[y-1][x-1]
        return count


board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

s = Solution()
s.gameOfLife(board)