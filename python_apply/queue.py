class Queue:
    def __init__(self):
        self.items = []
    def __repr__(self):
        return '<Queue object >'
    def __len__(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            self.items.pop(0)
        return 'Queue Empty'
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return 'Queue Empty'
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        return 'Queue Empty'
    def get_items(self):
        if not self.is_empty():
            return self.items
        return 'Queue Empty'

q = Queue()
print(q.get_items())
q.push('A')
q.push('B')
q.push('C')
q.push('D')
q.push('E')
print(len(q))
print(q.get_items())
q.pop()
print(len(q))
print(q.get_items())
q.pop()
print(len(q))
print(q.get_items())
print(q.front())
print(q.rear())