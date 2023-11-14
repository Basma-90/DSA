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

# priority queue using linked list
class priority_queue:
    def __init__(self):
        self.items = LinkedList()
    
    def enqueue(self,value,priority):
        self.items.insertRandom(value,priority)
    
    def dequeue(self):
        return self.items.deleteBegin()
    
    def empty(self):
        return self.items.size()==0
    
    def size(self):
        return self.items.size()
    
    def peek(self):
        return self.items.head.data
    
    def printQueue(self):
        self.items.printList()

'''
if __name__ == '__main__':
    priority_queue = priority_queue()
    priority_queue.enqueue(1,0)
    priority_queue.enqueue(6,1)
    priority_queue.enqueue(3,2)
    priority_queue.enqueue(4,3)
    priority_queue.printQueue()
'''
# to make only 3 priority as the task
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

class priorityQueue:
    def __init__(self):
        self.priority1=queue()
        self.priority2=queue()
        self.priority3=queue()

    def enqueue(self, item, priority):
        if priority == 1:
            self.priority1.enqueue(item)
        elif priority == 2:
            self.priority2.enqueue(item)
        elif priority == 3:
            self.priority3.enqueue(item)
        else:
            print("Invalid priority")

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        if not self.priority3.isEmpty():
            return self.priority3.dequeue()
        elif not self.priority2.isEmpty():
            return self.priority2.dequeue()
        else:
            return self.priority1.dequeue()
        
    def isEmpty(self):
        return self.priority1.isEmpty() and self.priority2.isEmpty() and self.priority3.isEmpty()
    
    def size(self):
        return self.priority1.size() + self.priority2.size() + self.priority3.size()
    def display(self):
        print(self.priority3)
        print(self.priority2)
        print(self.priority1)

if __name__ == '__main__':
    priority_queue = priorityQueue()
    priority_queue.enqueue(1,3)
    priority_queue.enqueue(6,1)
    priority_queue.enqueue(3,2)
    priority_queue.enqueue(4,3)
    priority_queue.display()
    print(priority_queue.dequeue())
    print(priority_queue.dequeue())
    print(priority_queue.dequeue())
    print(priority_queue.dequeue())
