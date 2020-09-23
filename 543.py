# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # max path from left subtree
        # max path from right subtree
        max_depth,max_path =  self.diameterOfBinaryTreeRecurring(root)
        if max_depth > max_path:
            max_path = max_depth
        return max_path
    def diameterOfBinaryTreeRecurring(self, root: TreeNode):
        if root is None:
            return 0,0
        if root.left and root.right:
            lmax_depth, lmax_path = self.diameterOfBinaryTreeRecurring(root.left)
            rmax_depth, rmax_path = self.diameterOfBinaryTreeRecurring(root.right)
            lmax_depth +=1
            rmax_depth += 1
            largest_path_candidate = lmax_depth+rmax_depth
            if largest_path_candidate > lmax_path and largest_path_candidate > rmax_path:
                return max(lmax_depth, rmax_depth), largest_path_candidate
            else:
                return max(lmax_depth, rmax_depth), max(lmax_path, rmax_path)
        elif root.left:
            lmax_depth, lmax_path = self.diameterOfBinaryTreeRecurring(root.left)
            lmax_depth += 1
            if lmax_path < lmax_depth:
                lmax_path = lmax_depth
            return lmax_depth, lmax_path
        elif root.right:
            rmax_depth, rmax_path = self.diameterOfBinaryTreeRecurring(root.right)
            rmax_depth += 1
            if rmax_path < rmax_depth:
                rmax_path = rmax_depth 
            return rmax_depth, rmax_path
        return 0,0


t = TreeNode(1,None, TreeNode(2,None,None))

s = Solution()
print(s.diameterOfBinaryTree(t))