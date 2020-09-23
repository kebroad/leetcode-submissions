# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return None
        l = self.findTiltRecursive(root.left)
        r = self.findTiltRecursive

        return abs(l - r)

    def findTiltRecursive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        s = root.val
        if root.left:
            s += self.findTiltRecursive(root.left)
        if root.right:
            s += self.findTiltRecursive(root.right)
        return s

        