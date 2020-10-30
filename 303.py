from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = []
        if len(nums) >= 1:
            self.sums.append(nums[0])
            for i in range(1, len(nums)):
                self.sums.append(nums[i]+self.sums[i-1])
        
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-1])

print(obj.sumRange(0,0))
#print(obj.sumRange(2, 5))
#print(obj.sumRange(0, 5))
print("kevin")