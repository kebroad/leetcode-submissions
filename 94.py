from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Recursive function. TODO: iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list = []
        if root is None:
            return None
        if root.left:
            list +=self.inorderTraversal(root.left)
        list.append(root.val)
        if root.right:
            list+=self.inorderTraversal(root.right)
        
        return list