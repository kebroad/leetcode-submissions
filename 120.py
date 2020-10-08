from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for row in range(n-2,-1,-1):
            for j in range(0, len(triangle[row])):
                triangle[row][j] = min(triangle[row+1][j],triangle[row+1][j+1]) + triangle[row][j]
        return triangle[0][0]
        #return self.minimumTotalRecurBetter(triangle, 0, 0)


    # def minimumTotalRecur(self, triangle: List[List[int]], low, high) -> List[List[int]]:
    #     top = triangle.pop(0)
    #     if triangle:
    #         l = []
    #         for i in range(low,high+1):
    #             l_j = self.minimumTotalRecur(triangle.copy(),i,i+1)
    #             l_j = [(j + top[i]) for j in l_j]
    #             l.extend(l_j)
    #         return [min(l)]
    #     else:
    #         return [top[low], top[high]]

    def minimumTotalRecurBetter(self, triangle: List[List[int]], low, high) -> int:
        top = triangle.pop(0)
        if triangle:
            l = []
            for i in range(low,high+1):
                l_j = self.minimumTotalRecurBetter(triangle.copy(),i,i+1)
                l_j = l_j + top[i]
                l.append(l_j)
            return min(l)
        else:
            return min(top[low], top[high])



i = [[1],[-2,-5],[3,6,9],[-1,2,4,-3]]
s = Solution()

print(s.minimumTotal(i))