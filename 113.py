# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return None
        return self.pathSumRecur(root, sum, [])

    def pathSumRecur(self, root: TreeNode, sum: int, path: List) -> List[List[int]]: 
        if not root.left and not root.right:
            if sum == root.val:
                path.append(root.val)
                return [path]
            else:
                return []
        l = []
        sum -= root.val
        path.append(root.val)
        if root.left:
            l.extend(self.pathSumRecur(root.left, sum, path.copy()))
        if root.right:
            l.extend(self.pathSumRecur(root.right, sum, path.copy()))
        return l

        

