# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if (root.val == 0) and (not self.containsOne(root.left) and not self.containsOne(root.right)):
            return None
        else:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
        return root

    def containsOne(self, root):
        if root is None:
            return False
        l = self.containsOne(root.left)
        r = self.containsOne(root.right)
        return l or r or (root.val == 1)

t = TreeNode(1, None, TreeNode(0, TreeNode(0, None,None), TreeNode(1,None,None)))

s = Solution()
s.pruneTree(t)