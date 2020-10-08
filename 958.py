# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        if self is None:
            return "None"
        return "TreeNode Val: "  + self.val + "Left: " + self.left + self.right 
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        qa = [root]
        parents = 1
        lastrow = False
        while len(qa) > 0:
            qb = []
            pathbroken = False
            while len(qa) > 0:
                el = qa.pop(0)
                if el.left:
                    qb.append(el.left)
                if el.right:
                    qb.append(el.right)
                if (not el.left) or ((not el.right) and (len(qa) != 0)):
                    pathbroken = True
            # children = len(qb)
            if lastrow:
                return False
            if pathbroken == True and len(qb) != 0:
                lastrow = True
            else:
                pathbroken = False

            # if (children != 0) and (children < ((2**parents)-1)) and (not lastrow):
            #     lastrow = True
            # parents = children
            qa = qb.copy()
        # if pathbroken:
        #     return False
        if lastrow:
            return False
        return True


#[1,2,3,5,6]

t = TreeNode(1, TreeNode(2,TreeNode(4,None,None), TreeNode(5,None,None)),TreeNode(3,None,None))

s = Solution()
print(s.isCompleteTree(t))