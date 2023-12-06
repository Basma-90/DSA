class Heap:
    def __init__(self):
        self.array=[]
        self.size=0
    
    def empty(self):
        return self.size==0
    
    def rightChild(self,i):
        if 2*i+2>=self.size:
            return -1
        return 2*i+2
    
    def leftChild(self,i):
        if 2*i+1>=self.size:
            return -1
        return 2*i+1
    
    def parent(self,i):
        if i<=0 or i>=self.size:
            return -1
        return (i-1)//2
    
    #i here is the index of the element to be heapified(child position)
    def heapify(self,i):
        parentPosition=self.parent(i)
        if i==0 or self.array[i]>self.array[parentPosition]:
            return
        self.array[i],self.array[parentPosition]=self.array[parentPosition],self.array[i]
        self.heapify(parentPosition)
    
    def push(self,data):
        if self.size+1>=len(self.array):
            self.array.append(None)
        self.array[self.size]=data
        self.size+=1
        self.heapify(self.size-1)
    
    def top(self):
        assert not self.empty()
        return self.array[0]
    
    def heapifyForRemove(self,position):
        lChild=self.leftChild(position)
        rChild=self.rightChild(position)
        if lChild==-1:
            return
        if rChild!=-1 and self.array[rChild]<self.array[lChild]:
            lChild=rChild
        if self.array[position]>self.array[lChild]:
            self.array[position],self.array[lChild]=self.array[lChild],self.array[position]
            self.heapifyForRemove(lChild)
    
    def pop(self):
        assert not self.empty()
        self.size-=1
        result=self.array[0]
        self.array[0]=self.array[self.size]
        self.heapifyForRemove(0)
        return result
    
    def printHeap(self):
        while not self.empty():
            print(self.pop())

if __name__=="__main__":
    heap=Heap()
    heap.push(2)
    heap.push(17)
    heap.push(22)
    heap.push(10)
    heap.push(8)
    heap.push(37)
    heap.push(14)
    heap.push(19)
    heap.push(7)
    heap.push(6)
    heap.push(5)
    heap.push(12)
    heap.push(25)
    heap.push(30)
    heap.printHeap()
    # 2, 5, 12, 8, 6, 14, 22, 19, 17, 10, 7, 37, 25, 30
    print("**********")
    heap2=Heap()
    heap2.push(2)
    heap2.push(17)
    heap2.push(22)
    heap2.pop()
    heap2.printHeap()
    # 5, 6, 12, 8, 7, 14, 22, 19, 17, 10, 30, 37, 25
    print("**********")
    heap3=Heap()
    heap3.push(2)
    heap3.push(17)
    heap3.push(22)
    heap3.push(10)
    heap3.push(8)
    heap3.push(37)
    heap3.push(14)
    heap3.push(19)
    heap3.push(7)
    heap3.push(6)
    heap3.push(5)
    heap3.push(12)
    heap3.push(25)
    heap3.push(30)
    heap3.pop()
    heap3.pop()
    heap3.pop()
    heap3.printHeap()


