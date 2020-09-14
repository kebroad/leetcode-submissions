# Definition for singly-linked list.
# https://www.youtube.com/watch?v=gE0GopCq378&ab_channel=mycodeschool
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = self.listLength(headA)
        len_b = self.listLength(headB)
        if(len_a > len_b):
            diff = len_a - len_b
            for _ in range(diff):
                headA = headA.next
        elif(len_b > len_a):
            diff = len_b - len_a
            for _ in range(diff):
                headB = headB.next
        while headA and headB:
            if headA is headB:
                return headB
            headA = headA.next
            headB = headB.next
        return None

        
    def listLength(self, head: ListNode) -> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count



s = Solution()
l = ListNode(1)
l.next = ListNode(2)
print(s.listLength(l))

