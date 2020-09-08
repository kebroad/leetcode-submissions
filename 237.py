# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node_curr = node.next
        node_prev = node
        while node_curr.next:
            node_prev.val = node_curr.val
            node_curr = node_curr.next
            node_prev = node_prev.next
        node_prev.val = node_curr.val
        del node_curr
        node_prev.next = None