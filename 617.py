# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3 = TreeNode()
        if (t1 is None) and (t2 is None):
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        t3.val = t1.val + t2.val
        t3.right = self.mergeTrees(t1.right, t2.right)
        t3.left = self.mergeTrees(t1.left, t2.left)
        return t3