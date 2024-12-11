class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next= node3
          
current = node1
while current:
    print(current.data)
    current = current.next


    def count(head):
       count = 0
       current = head
       while current:
           count += 1
           current = current.next
       return count   
count(node3)   