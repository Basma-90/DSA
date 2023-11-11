class deque:
    def __init__(self,size):
        self.added_items=0
        self.front=self.rear=0
        self.array=[None]*max(1,size)
    
    def full(self):
        return self.added_items==len(self.array)
    
    def prev(self,pos):
        pos-=1
        if pos==-1:
            pos=len(self.array)-1
        return pos
    
    def next_pos(self,pos):
        pos+=1
        if pos==len(self.array):
            pos=0
        return pos
    
    def add_front(self,item):
        assert not self.full()
        self.front=self.prev(self.front) 
        self.array[self.front]=item
        self.added_items+=1
        
    def add_rear(self,item):
        assert not self.full()
        self.array[self.rear]=item
        self.rear=self.next_pos(self.rear)
        self.added_items+=1
        
    def empty(self):
        return self.added_items==0
    
    def deque_front(self):
        assert not self.empty()
        value=self.array[self.front]
        self.front=self.next_pos(self.front)
        self.added_items-=1
        return value
    
    def deque_rear(self):
        assert not self.empty()
        self.rear=self.prev(self.rear)
        value=self.array[self.rear]
        self.added_items-=1
        return value
    
    def display(self):
        cur=self.front
        for i in range (self.added_items):
            print(self.array[cur],end=" ")
            cur=self.next_pos(cur)
        



