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
            self.head = self.head.next

    def deleteEnd(self):
        if self.last is None:
            print("linkedList is empty")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.last = temp

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
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next


if __name__ == '__main__':
    linkedList = LinkedList()

    # insert at begin
    linkedList.insertBegin(10)
    linkedList.insertBegin(20)
    linkedList.insertBegin(30)
    linkedList.insertBegin(40)
    linkedList.insertBegin(50)
    linkedList.insertBegin(50)
    linkedList.printList()
    print("\n")

    # insert at end
    linkedList.insertEnd(60)
    linkedList.insertEnd(70)
    linkedList.printList()
    print("\n")

    # insert at random
    linkedList.insertRandom(80, 3)
    linkedList.printList()
    print("\n")

    # search
    print(linkedList.search(80))

    # delete at begin
    linkedList.deleteBegin()
    linkedList.printList()

    # delete at end
    linkedList.deleteEnd()
    linkedList.printList()
    print("\n")

    # delete at random
    linkedList.deleteRandom(2)
    linkedList.printList()
    print("\n")

    # size
    print(linkedList.size())

    # isExist
    print(linkedList.isExist(80))
    print(linkedList.isExist(100))
