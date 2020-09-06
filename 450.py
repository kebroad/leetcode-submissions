# Definition for a binary tree node.
#https://www.youtube.com/watch?v=gcULXE7ViZw
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1: no Child - can delete leaf node
            if(root.left is None) and (root.right is None):
                del root #remove from memory
                root = None #point to null
            elif root.left is None:
                temp = root
                root = root.right
                del temp
            elif root.right is None:
                temp = root
                root = root.left
                del temp
            else: #two children
                temp = self.findMin(root.right) 
                #can also do findMax on left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root
            
    def findMin(self, root: TreeNode) -> TreeNode:
        while root.left is not None:
            root = root.left
        return root



