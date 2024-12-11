class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rare = None
        
    def enqueue(self,value):
        new_node = Node(value)
        if self.rare == None:
            self.front = new_node
            self.rare = self.front
        else:
            self.rare.next = new_node
            self.rare = new_node
    def dequeue(self):
        if self.front == None:
            print('empty queue')
        else:
            self.front = self.front.next
            
    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data)
            temp = temp.next
            
    def isEmpty(self):
        return self.front == None
    
    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            counter += 1
            temp = temp.next
        return 'size of Queue: ' , counter
    
    def frontitem(self):
        if self.front == None:
            print('empty')
        else:
          return 'front item is: ', self.front.data
    
    def rareitem(self):
        if self.front == None:
            print('empty')
        else:
          return 'rare item is: ', self.rare.data
                  
            
            
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(6)
q.enqueue(8)
q.traverse()
print(q.size())
print(q.frontitem())
print(q.rareitem())