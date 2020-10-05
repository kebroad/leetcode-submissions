# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        nums = self.sumNumbersRecur(root, "")
        return sum(nums)


    def sumNumbersRecur(self, root: TreeNode, s : str):
        l = []
        s += str(root.val)
        if root.left:
            l.extend(self.sumNumbersRecur(root.left, s))
        if root.right:
            l.extend(self.sumNumbersRecur(root.right, s))
        if not root.right and not root.left:
            return [int(s)]
        return l


s = Solution()
s.sumNumbe
