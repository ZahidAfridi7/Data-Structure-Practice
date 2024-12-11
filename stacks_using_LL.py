class  Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stacke:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next
    
    def peek(self):
        if (self.isEmpty()):
            return "stack is empty"
        else:
            return self.top.data
    def pop(self):
        if(self.isEmpty()):
            return "stsck is empty"
        else:
           self.top = self.top.next        

s = Stacke()
s.push(11)
s.push(12)
s.push(13)
s.push(14)
                           