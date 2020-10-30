from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        l = []
        self.combinationSumRecur(candidates, target, [], 0, l)
        return l


            


    def combinationSumRecur(self, candidates: List[int], target: int,  sublist: List[int], index: int, finallist: List[List[int]]):        
        if index > len(candidates)-1:
            return
        if target == 0:
            finallist.append(sublist.copy())
        s = target - candidates[index]
        if s >= 0:
            sublist_i = sublist.copy()
            sublist_i.append(candidates[index])
            self.combinationSumRecur(candidates,s, sublist_i, index, finallist)
            index+= 1
            if sublist_i:
                s += sublist_i.pop()
                self.combinationSumRecur(candidates,s, sublist_i.copy(), index, finallist)
        


s = Solution()
print(s.combinationSum([2,7,6,3,5,1], 9))