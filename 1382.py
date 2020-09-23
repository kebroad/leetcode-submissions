# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        l = self.inorderTraversal(root)
        start = 0
        end = len(l)-1
        return self.build(start,end,l)

    def build(self,start,end, l: list):
        if start > end:
            return None
        if start == end: 
            return TreeNode(l[start], None, None)
        if end-start == 2:
            mid = (end-start)//2
            root = TreeNode(l[start], None, None)
            left = TreeNode(l[mid], None, None)
            right = TreeNode(l[end], None, None)
            root.left = left
            root.right = right
            return root
        elif end-start == 1:
            root = TreeNode(l[start],None,None)
            right = TreeNode(l[end], None, None)
            root.right = right
            return root
        else:
            mid = (end+start) // 2
            root = TreeNode(l[mid], None,None)
            root.left = self.build(start,mid-1,l)
            root.right = self.build(mid+1,end,l)
            return root


    def inorderTraversal(self, root):
        l = []
        if root is None:
            return l
        if root.left:
            l.extend(self.inorderTraversal(root.left))
        l.append(root.val)
        if root.right:
            l.extend(self.inorderTraversal(root.right))
        return l
#[1,null,15,14,17,7,null,null,null,2,12,null,3,9,null,null,null,null,11]
s = Solution()
#t = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, None))))
t = TreeNode(1,None,None)
t.right = TreeNode(15,None,None)
t.right.left = TreeNode(14,None,None)
t.right.right = TreeNode(17,None,None)
t.right.left.left = TreeNode(7,None,None)
t.right.left.left.left = TreeNode(2,None,None)
t.right.left.left.right = TreeNode(12,None,None)
t.right.left.left.left.right = TreeNode(3,None,None)
t.right.left.left.right.left = TreeNode(9,None,None)
t.right.left.left.right.left.right = TreeNode(11,None,None)

l = []
#print(s.inorderTraversal(t))
print(s.balanceBST(t))