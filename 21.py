from typing import List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        if (not l1) and (not l2):
            return None
        elif not l1:
            l3.val = l2.val
            l3.next = l2.next
        elif not l2:
            l3.val = l1.val
            l3.next = l1.next
        elif l1.val < l2.val:
            l3.val = l1.val
            l3.next = self.mergeTwoLists(l1.next, l2)
        else:
            l3.val = l2.val
            l3.next = self.mergeTwoLists(l1, l2.next)            
        
        return l3