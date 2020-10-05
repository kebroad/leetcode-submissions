# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        return self.binaryTreeRecur(root, "")
        
    def binaryTreeRecur(self, root: TreeNode, s: str):
        l = []
        s += str(root.val)
        if root.left:
            l.extend(self.binaryTreeRecur(root.left, s + "->"))
        if root.right:
            l.extend(self.binaryTreeRecur(root.right, s + "->"))
        if not root.right and not root.left:
            return [s]
        return l