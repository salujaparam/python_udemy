class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

class DoublyList:
    def __init__(self):
        self.head = Node()
    def append(self, data):
        cur = self.head
        new_node = Node(data)
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def length(self):
        cur = self.head
        l = 0
        while cur.next!=None:
            cur = cur.next
            l+=1
        return l
    def get_list(self):
        items = []
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            items.append(cur.data)
        return items

    def second_last(self):
        cur = self.head
        while cur.next!=None:
            cur=cur.next
        second_last = cur.prev
        return second_last.data

d = DoublyList()
d.append(1)
d.append(2)
d.append(3)
print(d.length())
print(d.get_list())
print(d.second_last())