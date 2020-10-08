# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        chead = rhead = ListNode(0, None)
        rhead.next = head
        vals = set()
        while chead.next:
            if chead.next.val in vals:
                if chead.next.next:
                    chead.next = chead.next.next
                else:
                    chead.next = None
                    break
            else:
                vals.add(chea  d.next.val)
                chead = chead.next
        return rhead.next
#[1,1,2,3,3]
l = ListNode(1, ListNode(1, ListNode(1, None)))
s = Solution()
s.deleteDuplicates(l)