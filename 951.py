# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # if root1 is None or root2 is None:
        #    return True
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        val1 = {}
        val2 = {}
        set1 = set()
        set2 = set()
        if root1.left:
            set1.add(root1.left.val)
            val1[root1.left.val] = root1.left
        if root1.right:
            set1.add(root1.right.val)
            val1[root1.right.val] = root1.right
        if root2.left:
            set2.add(root2.left.val)
            val2[root2.left.val] = root2.left
        if root2.right:
            set2.add(root2.right.val)
            val2[root2.right.val] = root2.right
        if len(set1) == 0 and len(set2) == 0:
            return True
        if set1 != set2 or (root1.val != root2.val):
            return False
        else:
            matches = []
            for key in val1:
                matches.append(self.flipEquiv(val1[key], val2[key]))
            return all(matches)