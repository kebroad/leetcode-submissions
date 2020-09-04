from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # thanks mycodeschool for the help :)
        #https://www.youtube.com/watch?v=4qjprDkJrjY&frags=wn&ab_channel=mycodeschool
        res = []
        top = 0 # topmost row
        bottom = len(matrix)-1 # bottommost row
        left = 0 #leftmost column
        right = len(matrix[0])-1 #rightmost column
        dir = 'r'
        while (top <= bottom) and (left <= right):
            if dir == 'r':
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top += 1
                dir = 'd'
            elif dir == 'd':
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right -= 1
                dir = 'l'
            elif dir == 'l':
                for i in range(right, left-1,  -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                dir = 'u'
            elif dir == 'u':
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
                dir = 'r'
        return res


s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))