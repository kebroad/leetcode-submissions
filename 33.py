#https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = high + low // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[high]: #if right half is sorted correctly
                if (target > nums[mid]) and (target <= nums[high]): #and targets inside of this sorted side
                    low = mid+1
                else: #targets on other (unsorted) side
                    high = mid-1
            elif nums[low] <= nums[mid]: #if left half is sorted correctly (in increasing order)
                if(target < nums[mid]) and (target >= nums[low]): #and targets inside this sorted half
                    high = mid - 1
                else: #targets on right unsorted half
                    low = mid + 1
        return -1

    
s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))