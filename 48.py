from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        high = len(matrix)-1
        low =  0
        while high > low:
            for offset in range(0,high-low):
                matrix[low][low+offset],matrix[low+offset][high] = matrix[low+offset][high],matrix[low][low + offset]
                matrix[high][high-offset],matrix[low][low+offset] = matrix[low][low+offset],matrix[high][high-offset]
                matrix[high-offset][low],matrix[low][low+offset] = matrix[low][low+offset],matrix[high-offset][low]
            high -= 1
            low += 1
        print('yuh')



#m = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
m = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]

s = Solution()
s.rotate(m)