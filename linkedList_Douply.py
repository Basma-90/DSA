class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linked_list:
    def __init__(self):
        self.head = None
        self.last = None
    def insertBegin(self,data):
        newNode = Node(data)
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.last = newNode
        else:
            newNode.next=self.head
            newNode.prev=None
            self.head.prev=newNode
            self.head=newNode

    def insertEnd(self,data):
        newNode = Node(data)
        if self.last is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.last = newNode
        else:
            newNode.next=None
            newNode.prev=self.last
            self.last.next=newNode
            self.last=newNode

    def insertRandom(self,data,position):
        newNode=Node(data)
        if position==0:
            self.insertBegin(data)
        elif position==self.size()-1:
            self.insertEnd(data)
        else:
            temp=self.head
            for i in range(position-1):
                if temp is None:
                    print("Index out of bound")
                    return
                temp=temp.next
            newNode.next=temp.next
            newNode.prev=temp
            temp.next=newNode
            newNode.next.prev=newNode

    def deleteBegin(self):
        if self.head is None:
            print("linkedList is empty")
        else:
            self.head=self.head.next
            self.head.prev=None

    def deleteEnd(self):
        if self.last is None:
            print("linkedList is empty")
        else:
            self.last=self.last.prev
            self.last.next=None

    def deleteRandom(self,position):
        if position==0:
            self.deleteBegin()
        elif position==self.size()-1:
            self.deleteEnd()
        else:
            temp=self.head
            for i in range(position-1):
                if temp is None:
                    print("Index out of bound")
                    return
                temp=temp.next
            temp.next=temp.next.next
            temp.next.prev=temp

    def size(self):
        temp=self.head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
    
    def search(self,data):
        temp=self.head
        index=0
        while temp is not None:
            if temp.data==data:
                return index
            index+=1
            temp=temp.next
        return -1
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def isExist(self,data):
        temp=self.head
        while temp is not None:
            if temp.data==data:
                return True
            temp=temp.next
        return False
    
if __name__ == "__main__":
    linked_list = linked_list()
    linked_list.insertBegin(10)
    linked_list.insertBegin(20)
    linked_list.insertBegin(30)
    linked_list.insertEnd(40)
    linked_list.insertEnd(50)
    linked_list.insertEnd(60)
    linked_list.insertRandom(70, 2)
    linked_list.insertRandom(80, 4)
    linked_list.display()
    print("\n")
    print(linked_list.search(80))
    linked_list.deleteBegin()
    linked_list.display()
    print("\n")
    linked_list.deleteEnd()
    linked_list.display()
    print("\n")
    linked_list.deleteRandom(3)
    linked_list.display()
    print("\n")
    print(linked_list.size())
    print(linked_list.isEmpty())
    print(linked_list.isExist(80))
    print(linked_list.isExist(100))
    


