# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = current = ListNode()
        carryover = 0
        while l1 or l2 or carryover:
            res = ListNode()
            if l1:
                carryover += l1.val
                l1 = l1.next
            if l2:
                carryover += l2.val
                l2 = l2.next
            current.next = current = ListNode(carryover % 10)
            if carryover >= 10:
                carryover = 1
            else:
                carryover = 0
        return root.next

    



    # def listToNum(self, head: ListNode) -> int:
    #     res = int(head.val)
    #     count = 0
    #     head = head.next
    #     while head.next is not None:
    #         res = res + 10*count*head.val
    #     return res

s = Solution()

