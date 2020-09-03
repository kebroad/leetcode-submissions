# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = reverse(l1)
        l2 = reverse(l2)




    def reverse(self, l1: ListNode):
        cur = l1.next
        prev = l1
        while cur.next is not None:
            cur = cur.next
            cur.next = prev
            prev = prev.next

        return prev

