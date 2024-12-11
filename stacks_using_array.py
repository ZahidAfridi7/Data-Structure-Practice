class Stack():
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1
    
    def push(self,value):
        if self.top == self.size - 1:
         print("overflow")
        else:
            self.top += 1
            self.stack[self.top] = value 
    def pop(self):
        if self.top == -1:
            print("empty")
        else:
            data = self.stack[self.top]
            self.top -= 1
            print(data)
    
    def traverse(self):
        for i in range(self.top + 1):
            print(self.stack[i], end=' ')        
                   
            
s = Stack(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
s.pop()
s.pop()
s.pop()
s.traverse()


        