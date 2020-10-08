class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#[1,2,3,3,4,4,5]

def listToLinkedList(nums):
    rhead = chead = ListNode(0,None)
    for num in nums:
        newNode = ListNode(num,None)
        chead.next = newNode
        chead = chead.next
    return rhead.next

def linkedListToList(l: ListNode):
    rlist = []
    while l:
        rlist.append(l.val)
        l = l.next
    return rlist



#l = listToLinkedList([1,2,3,3,4,4,5])