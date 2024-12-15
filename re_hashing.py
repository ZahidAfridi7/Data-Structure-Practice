class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.size = 0  
        self.bucket = self.make_array(self.capacity)  
        self.load_factor_threshold = 0.7  

    def make_array(self, capacity):
        """Create an empty array with the given capacity."""
        return [None] * capacity

    def hash_function(self, key):
        """Compute a hash value and map it to a valid index."""
        return abs(hash(key)) % self.capacity

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)  # Get the index for the key
        current = self.bucket[index]

        
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        
        new_node = Node(key, value)
        new_node.next = self.bucket[index]
        self.bucket[index] = new_node
        self.size += 1

        
        if self.size / self.capacity > self.load_factor_threshold:
            self.rehash()

    def rehash(self):
        
        print("Rehashing triggered. Doubling the table size...")
        old_bucket = self.bucket
        new_capacity = self.capacity * 2
        self.bucket = self.make_array(new_capacity)
        self.capacity = new_capacity
        self.size = 0 
        
        for head in old_bucket:
            current = head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def traverse(self):
        """Traverse the hash table and print all key-value pairs."""
        print("Hash Table Contents:")
        for i in range(self.capacity):
            print(f"Bucket {i}:", end=" ")
            current = self.bucket[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"({current.key}, {current.value})", end=" -> ")
                    current = current.next
                print("None")


# Testing the rehashing functionality
d = Dictionary(5)

# Insert key-value pairs
d.insert("apple", 100)
d.insert("banana", 200)
d.insert("cherry", 300)
d.insert("grape", 400)  # This will trigger rehashing
d.insert("orange", 500)

# Traverse and print the hash table after rehashing
d.traverse()
