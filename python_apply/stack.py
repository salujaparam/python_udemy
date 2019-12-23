class Stack:
    def __init__(self):
        self.items = []
    def  __repr__(self):
        return '<Stack object>'
    def __len__(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def is_empty(self):
        return self.items == []
    def pop(self):
        if not self.is_empty():
            self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'Stack empty'
    def get_stack(self):
        if not self.is_empty():
            return self.items
        return 'Stack empty'
    def empty_stack(self):
        if not self.is_empty():
            self.items = []


s = Stack()

print(s.get_stack())
s.push('Work')
print(s.get_stack())
s.push('play')
s.push('movies')
s.push('songs')
print(s.get_stack())
s.pop()
print(s.get_stack())
print(len(s))
s.empty_stack()
print(s.get_stack())
print(len(s))
print(s)
