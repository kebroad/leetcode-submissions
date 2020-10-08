# Definition for singly-linked list.
from linkedlists import ListNode, listToLinkedList, linkedListToList
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        rhead = chead = ListNode(0, None)
        chead.next = head
        counts = {}
        # pass 1, get count
        while chead.next:
            if chead.next.val in counts:
                counts[chead.next.val] = counts.get(chead.next.val) + 1
            else:
                counts[chead.next.val] = 1
            chead = chead.next
        chead = rhead
        while chead.next:
            if counts[chead.next.val] > 1:
                if chead.next.next:
                    chead.next = chead.next.next
                else:
                    chead.next = None
            else:
                chead = chead.next
        return rhead.next


#

l = listToLinkedList([1,2,3,3,4,4,5])
s = Solution()
l = s.deleteDuplicates(l)
print(linkedListToList(l))