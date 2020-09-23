# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        if not self.val:
            printval = "null"
        else:
            printval = str(self.val)
        if not self.left:
            leftval = "null"
        else:
            leftval = str(self.left.val)
        if not self.right:
            rightval = "null"
        else:
            rightval = str(self.right.val)
        return "TreeNode val: " + printval + "; left: " + leftval + "; right: " + rightval
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        s = ""
        if t is None:
            return t
        s = self.buildtree2str(t, s)
        #visit left
        #visit right
        n = len(s)
        # for i in range(0,s-3):
        #     if s[i:i+3] == '()()':
        #         s = s[0:i] + s[i+3:n-1]
        return s
    def buildtree2str(self, t: TreeNode, s: str) ->str:
        if t is None:
            return s
        s += str(t.val)
        s += '('
        s = self.buildtree2str(t.left, s)
        s += ')'
        if t.right:
            s += '('
            s = self.buildtree2str(t.right, s)
            s += ')'
        return s


t = TreeNode(1, TreeNode(2, None, TreeNode(4, None, None)), TreeNode(3, None, None))

s = Solution()
print(s.tree2str(t))