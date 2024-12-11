#creating nodes and joining them manually
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
#creating linkedlist

class Linked_list:
    def __init__(self):
        self.head = None
        self.n = 0
        
#creating len() function
    def __len__(self):
        return self.n

#inserting    
    def insert(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

#traversing(printing)

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]    

#appending

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node  
        self.n = self.n + 1  

#inserting in-between
    
    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return "item not found"        

#deleting-clear

    def clear(self):
        self.head = None
        self.n = 0

#delete-from-head
    def delete_head(self):
        if self.head == None:
            return "list already empty"
        self.head = self.head.next 
        self.n = self.n + 1       
            
#delete for tail
    def pop(self):
        curr = self.head
        if curr.next == None:
            return self.delete_head
        
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n + 1
                        
#deleting item by value

    def remove(self, value):
     curr = self.head
    
    # Handle empty list
     if curr is None:
        return "List is empty"
    
    # Handle if the head node contains the value
     if curr.data == value:
        self.head = curr.next
        return "Removed"
    
    # Traverse the list to find the node to remove
     while curr.next is not None:
        if curr.next.data == value:
            curr.next = curr.next.next  # Bypass the node
            return "Removed"
        curr = curr.next
    
    # If we reach here, the value was not found
     return "Not found"

#Searching by value
    def search(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "not found"    
#search by index
    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1
              
        
l = Linked_list()
l.insert(1)
l.insert(2)
l.insert(3)
l.append(5)
l.append(4)
print(l[4])
