# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlists import linkedListToList, listToLinkedList, ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if slow == head:
            if slow.next.val == head.val:
                return True
            else:
                return False
        mid2 = slow.next
        slow.next = None
        s2 = self.reverse(mid2)
        s1 = head
        while s1 and s2:
            if s1.val != s2.val:
                return False
            s1 = s1.next
            s2 = s2.next
        return True

    def reverse(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if not head.next:
            return head
        #dummy = ListNode(0,None)
        c = head.next
        p = head
        while c.next:
            temp = c.next
            c.next = p
            p = c
            c = temp
        c.next = p
        head.next = None
        return c
        

s = Solution()
l = listToLinkedList([1,0,0])
print(s.isPalindrome(l))
#print(linkedListToList(l2))