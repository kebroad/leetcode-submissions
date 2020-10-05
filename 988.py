# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root is None:
            return ""
        l = self.smallestFromLeafRecur(root, [])
        m = min(l)
        s = ""
        for num in m:
            s += chr(num+97)
        return s


    def smallestFromLeafRecur(self,root: TreeNode, q: list):
        l = []
        q.insert(0,root.val)
        if root.left:
            l.extend(self.smallestFromLeafRecur(root.left, q.copy()))
        if root.right:
            l.extend(self.smallestFromLeafRecur(root.right, q.copy()))
        if not root.left and not root.right:
            return [q]
        return l

t = TreeNode(0, TreeNode(1,TreeNode(3,None,None), TreeNode(4,None,None)), TreeNode(2,TreeNode(3,None,None), TreeNode(4,None,None)))

s = Solution()
print(s.smallestFromLeaf(t))
