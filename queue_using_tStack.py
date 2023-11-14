#implement a queue using two stacks
# tc of enqueue is O(1) and dequeue is O(1)
class stack:
    def __init__(self):
        self.items = []
    def push(self,value):
        self.items.append(value)
    def pop(self):
        assert self.items, 'No items!'
        return self.items.pop()
    def peek(self):
        assert self.items, 'No items!'
        return self.items[-1]
    def empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

class queue:
    def __init__(self):
        self.stk1 = stack()
        self.stk2 = stack()
    def move(self,stk1,stk2):
        while not stk1.empty():
            stk2.push(stk1.pop())
    def enqueue(self,value):
        self.move(self.stk1,self.stk2)
        self.stk1.push(value)
        self.move(self.stk2,self.stk1)
    def dequeue(self):
        assert not self.empty()
        value = self.stk1.pop()
        return value
    def empty(self):
        return self.stk1.empty()
if __name__=='__main__':
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    
