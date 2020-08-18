
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = (fast.next).next
        second = slow.next
        slow.next = None

        lista = self.sortList(head)
        listb = self.sortList(second)

        return self.merge(lista, listb)

    def merge(self, a : ListNode, b: ListNode) -> ListNode:
        if a is None:
            return b
        if b is None:
            return a
        final = ListNode()
        head = final
        while a and b:
            if a.val < b.val:
                head.next = a
                a = a.next
            else:
                head.next = b
                b= b.next
            head = head.next
        if a:
            head.next=a
        elif b:
            head.next = b

        return final.next

s = Solution()

h = a = ListNode(4, None)
a.next = ListNode(2, None)
a = a.next
a.next = ListNode(1, None)
a = a.next
a.next = ListNode(3,None)

print(s.sortList(h))


            

        