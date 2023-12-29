class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def isExist(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def search(self, data):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.data == data:
                return index
            index += 1
            temp = temp.next
        return -1

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def deleteBegin(self):
        if self.head is None:
            print("linkedList is empty")
        else:
            value=self.head.data
            self.head = self.head.next
            return value

    def deleteEnd(self):
        if self.last is None:
            print("linkedList is empty")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            value=temp.next.data
            temp.next = None
            self.last = temp
            return value

    def deleteRandom(self, position):
        if position == 0:
            self.deleteBegin()
        elif position == self.size() - 1:
            self.deleteEnd()
        else:
            temp = self.head
            for i in range(position - 1):
                if temp is None:
                    print("Index out of bound")
                    return
                temp = temp.next
            temp.next = temp.next.next

    def insertBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.next = None
            self.head = newNode
            self.last = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        if self.last is None:
            newNode.next = None
            self.head = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

    def insertRandom(self, data, position):
        if position == 0:
            self.insertBegin(data)
        else:
            newNode = Node(data)
            current = self.head
            for i in range(position - 1):
                if current is None:
                    print("Index out of bound")
                    return
                current = current.next
            newNode.next = current.next
            current.next = newNode

    def printList(self):
        temp = self.head
        if temp is None:
            return 
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

class queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.insertEnd(item)
    
    def dequeue(self):
        return self.queue.deleteBegin()
    
    def isEmpty(self):
        return self.queue.size() == 0
    
    def size(self):
        return self.queue.size()
    
    def peek(self):
        return self.queue.head.data
    
    def __str__(self):
        result = self.queue.printList()
        if result:
            return result[:-2]  
        else:
            return "" 

class deque:
    def __init__(self):
        self.deque = LinkedList()
    
    def addFront(self, item):
        self.deque.insertBegin(item)
    
    def addRear(self, item):
        self.deque.insertEnd(item)
    
    def removeFront(self):
        return self.deque.deleteBegin()
    
    def removeRear(self):
        return self.deque.deleteEnd()
    
    def isEmpty(self):
        return self.deque.size() == 0
    
    def size(self):
        return self.deque.size()
    
    def peekFront(self):
        return self.deque.head.data
    
    def peekRear(self):
        return self.deque.last.data
    
    def __str__(self):
        result = self.deque.printList()
        if result:
            return result[:-2]  
        else:
            return ""

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)
v = q.dequeue()
print(v)
print(q)
print(q.peek())
print(q.isEmpty())
print(q.size())

d=deque()
d.addFront(10)
d.addFront(20)
d.addRear(30)
d.addRear(40)
print(d)
print(d.peekFront())
print(d.peekRear())
print(d.removeFront())
print(d.removeRear())
print(d)
print(d.isEmpty())
print(d.size())
