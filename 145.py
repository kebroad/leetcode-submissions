# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        list = []
        if root is None:
            return None
        if root.left:
            list += self.postorderTraversal(root.left)
        if root.right:
            list += self.postorderTraversal(root.right)
        list.append(root.val)
        return list