class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.table = [None] * self.size  
          
    def search(self, key):
        index = self._hash(key)  
        current = self.table[index]  
        
       
        while current:
            if current.key == key:
                return current.value  
            current = current.next  
        return None  
 
    
    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self.hash_function(key)  # Get the index for the key
        current = self.bucket[index]  # Start at the head node
        prev = None  # Previous node to help with deletion

        # If the head node contains the key, use delete_head
        if current and current.key == key:
            return self.delete_head(key)  # Delete the head node

        # Traverse the linked list to find the key
        while current:
            if current.key == key:
                # Found the key, remove it by updating the previous node's next
                prev.next = current.next
                self.size -= 1
                return True
            prev = current  # Move prev to current
            current = current.next  # Move current to the next node

        return False  # Key not found

    
    def __setitem__(self, key, value):
        """Allows ht[key] = value."""
        self.insert(key, value)

    def __getitem__(self, key):
        """Allows ht[key]. Raises KeyError if key is not found."""
        result = self.search(key)
        if result is None:
            raise KeyError(f"Key {key} not found.")
        return result

    def __delitem__(self, key):
        """Allows del ht[key]. Raises KeyError if key is not found."""
        if not self.delete(key):
            raise KeyError(f"Key {key} not found.")

    def __contains__(self, key):
        """Allows 'key in ht'."""
        return self.search(key) is not None

class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.size = 0  
        self.bucket = self.make_array(self.capacity)  

    def make_array(self, capacity):
        """Create an empty array with the given capacity."""
        L = []  
        for i in range(capacity):
            L.append(None)  
        return L

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

    def hash_function(self, key):
      return abs(hash(key)) % self.capacity


    def get_index_at_node(self, key):
        """Find the index and node of a given key."""
        index = self.hash_function(key)  
        current = self.bucket[index] 
        while current:
            if current.key == key:  
                return index
            current = current.next  

        return None  # Key not found  
    
    
    def get(self, key):
        """Retrieve the value associated with the given key."""
        index = self.hash_function(key)  # Get the index for the key
        current = self.bucket[index]  # Start at the head of the chain at this index

        # Traverse the linked list to find the key
        while current:
            if current.key == key:
                return current.value  # Key found; return its value
            current = current.next  # Move to the next node in the chain

        return None  # Key not found
    
    def delete_head(self, key):
        """Delete the head node at the given key."""
        index = self.hash_function(key)  # Get the index for the key
        current = self.bucket[index]  # Get the head node at this index
        
        # If the bucket is empty, there's nothing to delete
        if not current:
            return False
        
        # If the key is found in the head node
        if current.key == key:
            # Remove the head node by pointing to the next node
            self.bucket[index] = current.next
            self.size -= 1
            return True
        
        return False  # Key not found at the head
    
              

# Create a dictionary
d = Dictionary(5)

# Add linked list nodes manually for demonstration
d.bucket[0] = Node("apple", 100)
d.bucket[0].next = Node("banana", 200)

d.bucket[2] = Node("cherry", 300)

# Traverse and print the hash table
d.traverse()
                