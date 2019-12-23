class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = Node()
        self.last = None
    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        cur = self.head
        if self.last == None:
            cur.next = new_node
            self.last = new_node
        else:
            while cur.next!=self.last:
                cur = cur.next
            cur.next = new_node
            self.last = new_node
    def get_list(self):
        cur = self.head
        cur = cur.next
        items = []
        while cur.data!=None:
            items.append(cur.data)
            cur = cur.next
        return items
c = CircularList()
c.append(1)
c.append(2)
c.append(3)
print(c.get_list())

    