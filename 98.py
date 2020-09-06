#https://www.youtube.com/watch?v=yEwSGhSsT0U

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecur(root,  -100000000000000000000, 1000000000000000000 )

    def isValidBSTRecur(self, root: TreeNode, min: int, max: int):
        if root is None:
            return True
        if (root.val > min) and (root.val < max) and self.isValidBSTRecur(root.left, min , root.val) and self.isValidBSTRecur(root.right, root.val, max):
            return True
        else:
            return False


t = TreeNode(2, TreeNode(1), TreeNode(3))
s = Solution()
print(s.isValidBST(t))



