class stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return (self.stack == [])
    def size(self):
        return len(self.stack)
    def peek(self):
        return self.stack[-1]
    def __str__(self):
        return str(self.stack)
s = stack()
s.push(10)
s.push(20)
s.push(30)
print(s)
s.pop()
print(s)
print(s.peek())
print(s.isEmpty())
print(s.size())
# Output:
# [10, 20, 30]
# [10, 20]
# 20
# False
# 2
