class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stacke:
    def __init__(self):
        self.top = None
        self.count = 0  # To track the size of the stack
    
    def isEmpty(self):
        return self.top == None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1  # Increment size
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            popped_data = self.top.data
            self.top = self.top.next
            self.count -= 1  # Decrement size
            return popped_data  # Return the popped value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.top.data

    def size(self):
        return self.count
    
    def traverse(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def find_celebrity(matrix):
    n = len(matrix)
    s = Stacke()

    # Push all people onto the stack
    for i in range(n):
        s.push(i)

    # Eliminate non-celebrities
    while s.size() >= 2:
        i = s.pop()
        j = s.pop()

        if matrix[i][j] == 0:
            # i doesn't know j, so i could still be a celebrity
            s.push(i)
        else:
            # i knows j, so i can't be a celebrity
            s.push(j)

    # Check the last remaining person
    if s.isEmpty():
        return "No celebrity found"
    
    candidate = s.pop()

    # Verify the candidate
    for i in range(n):
        if i != candidate and (matrix[candidate][i] == 1 or matrix[i][candidate] == 0):
            return "No celebrity found"
    
    return f"Celebrity is person {candidate}"

# Test case
l = [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

print(find_celebrity(l))
                     