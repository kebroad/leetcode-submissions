from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        length = len(matrix)
        width = len(matrix[0])
        for j in range(length):
            for i in range(width):
                if matrix[j][i] == 0:
                    zero_cols.add(i)
                    zero_rows.add(j)
        for j in range(length):
            for i in range(width):
                if (j in zero_rows) or (i in zero_cols):
                    matrix[j][i] = 0

m = [
[0,1,2,0],[3,4,5,2],[1,3,1,5]
]


s = Solution()
s.setZeroes(m)
print(m[0])
print(m[1])
print(m[2])