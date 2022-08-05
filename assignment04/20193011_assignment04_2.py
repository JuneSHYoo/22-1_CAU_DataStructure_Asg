# 원형큐 구성

MAX_SIZE = 20 

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0 
        self.items = [None]*MAX_SIZE
        
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear+1)%MAX_SIZE
    
    def clear(self):
        self.front = self.rear
        
    def enqueue( self, item) :
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_SIZE
            self.items[self.rear] = item
            print(f"(SYSTEM) ADDQUEUE({item}) F={self.front}, R={self.rear}")
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_SIZE
            print(f"DELETEQUEUE() = {self.items[self.front]} ,F={self.front}, R={self.rear}")
            return self.items[self.front]
        
        else:
            print("DELETEQUEUE( ) FAIL. QueueEmpty")
            
        
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_SIZE]
        
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1: self.rear+1]
        else :
            out = self.items[self.front+1:MAX_SIZE]+self.items[0:self.rear+1]
        if not self.isEmpty():
            print(f"QUEUE = {''.join(out)}({len(out)})")
        else :
            print("QUEUE = (0)")
        
# 큐 실행
q = CircularQueue()
count =0 
while 1:
    x = input()
    if(x >= '0' and x <= '9'):
        x = int(x)
        if x == 0:
            q.display()
        else:
            for i in range(x):
                q.dequeue()     
    else:
        x = list(x)
        for i in x:
            q.enqueue(i)
            count += 1 
    
    if q.isEmpty() == True and count != 0:
        break