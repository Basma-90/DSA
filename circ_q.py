class queue:
    def __init__(self,size):
        self.front=self.rear=0
        self.added_items=0
        self.array=[None]*max(1,size)
    
    def is_empty(self):
        return self.added_items==0
    
    def is_full(self):
        return self.added_items==len(self.array)
    
    def next_pos(self,pos):
        size=len(self.array)
        return (pos+1)%size
    
    def enqueue(self,value):
        assert not self.is_full()
        self.array[self.rear]=value
        self.rear=self.next_pos(self.rear)
        self.added_items+=1

    def dequeue(self):
        assert not self.is_empty()
        value=self.array[self.front]
        self.front=self.next_pos(self.front)
        self.added_items-=1
        return value
    
    def display(self):
        CURRENT =self.front
        for i in range(self.added_items):
            print(self.array[CURRENT],end=" ")
            CURRENT=self.next_pos(CURRENT)
    

if __name__ == '__main__':
    queue=queue(6)
    assert queue.is_empty()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.dequeue()
    queue.display()


