
# Definition for a Node.
class Node:
    def __init__(self, x: int, y: int, next: 'Node' = None, prev: 'Node' = None):
        self.key = int(x)
        self.val = int(y)
        self.next = next
        self.prev = prev
    def __str__(self):
        return "Node key: " + str(self.key)
    def __repr__(self):
        return "Node key: " + self.key
class LRUCache:

    def __init__(self, capacity: int):
        self.cur_capacity = 0
        self.full_capacity = capacity
        self.start = None
        self.end = None
        self.loc = {}

    def get(self, key: int) -> int:
        if key in self.loc:
            # replace end to node of list
            cur = self.loc[key]
            if cur != self.end:
                if cur.next and cur.prev:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                if cur == self.start:
                    self.start = cur.next
                self.end.next = cur
                cur.prev = self.end
                self.end = cur
                cur.next = None
            if(self.start.prev):
                self.start.prev = None
            return (self.loc[key]).val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.loc:
            # replace end to node of list
            cur = self.loc[key]
            if cur != self.end:
                cur.val = value
                if cur.next and cur.prev:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                if cur == self.start:
                    self.start = cur.next
                if cur == self.end:
                    pass
                else:
                    self.end.next = cur
                    cur.prev = self.end
                    self.end = cur
                    cur.next = None
                if(self.start.prev):
                    self.start.prev = None
            else:
                self.end.val = value
        elif self.start is None:
            self.start = self.end = Node(key,value, None, None)
            self.cur_capacity += 1
        elif self.cur_capacity < self.full_capacity:
            self.end.next = Node(key, value, None, self.end)
            self.end = self.end.next
            self.loc[key] = self.end
            self.cur_capacity += 1
        else:
            #full cache with new item, evict last used
            self.end.next = Node(key, value, None, self.end)
            self.end = self.end.next 
            temp = self.start
            self.start = self.start.next
            self.start.prev = None
            self.loc.pop(temp.key)
            del temp
        self.loc[key] = self.end

            
l = LRUCache(2)
print(l.put(1,1))
print(l.put(2,2))
print(l.get(1))
print(l.put(3,3))
print(l.get(2))
print(l.put(4,4))
print(l.get(1))
print(l.get(3))
print(l.get(4)        )


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
