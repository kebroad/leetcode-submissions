from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            interior = sum(distance[start:destination])
            exterior = sum((distance[0:start]) + distance[destination:len(distance)])
        else:
            interior = sum(distance[destination:start])
            exterior = sum((distance[0:destination]) + distance[start:len(distance)])
        return min(interior, exterior)

s = Solution()
print(s.distanceBetweenBusStops([7,10,1,12,11,14,5,0],7,2))