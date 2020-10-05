from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0], None, None)
        if n == 2:
            return TreeNode(nums[0], None, TreeNode(nums[1], None, None))
        else:
            mid = n // 2
            root = TreeNode(nums[mid], None, None)
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:n])
            return root

            
s = Solution()
s.sortedArrayToBST([-10,-3,0,5,9])
