
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        m = {}
        chead = rhead = Node(0,None,None)
        while head is not None:
            if head in m: #existing node
                addr = m[head]
                addr.val = head.val
                addr.next = head.next
                addr.random = head.random
            else:
                addr = Node(head.val,None, None)
                m[head] =  addr
            chead.next = addr
            if head.random is not None:
                if head.random in m:
                    addr.random = m[head.random]
                else:
                    addr.random = Node(0, None, None)
                    m[head.random] = addr.random
            else:
                addr.random = None
            chead = addr
            head = head.next
        return rhead.next
node1 = Node(2, None, None)
node2 = Node(4, None, node1)
node3 = Node(5, None, None)
node1.random = node3
node2.random = node1
node2.next = node3
node1.next = node2
node3.random = None

s = Solution()
n = s.copyRandomList(node1)

while n != None:
    print("Val: " + str(n.val))
    print("Random: " + str(n.random))
    print("Next:" + str(n.next))
    print("~~~~~~~~~~~~")
    n = n.next