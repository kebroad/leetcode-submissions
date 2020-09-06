from typing import List
# https://www.youtube.com/watch?v=86g8jAQug04
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [None, root]
        final = []
        working = []
        while queue:
            e = queue.pop()
            if e == None:
                if queue:
                    if queue[0] != None:
                        queue.insert(0, None)
                final.append(working)
                working = []
            else:
                working.append(e.val)
                if e.left:
                    queue.insert(0,e.left)
                if e.right:
                    queue.insert(0,e.right)
        return final


t =  TreeNode(3, TreeNode(9), TreeNode(20))       
s = Solution()

print(s.levelOrder(t))