class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.table = [None] * self.size  # Create a table (array) of given size
        
    def _hash(self, key):
      return hash(key) % self.size  # Python's built-in hash function and modulo
      
    def search(self, key):
        index = self._hash(key)  # Calculate the index
        current = self.table[index]  # Start at the head of the linked list
        
        # Traverse through the list to find the key
        while current:
            if current.key == key:
                return current.value  # Return the value if key is found
            current = current.next  # Move to the next node in the chain
        return None  # Return None if the key is not found
 
    def delete(self, key):
        index = self._hash(key)  # Calculate the index
        current = self.table[index]  # Start at the head of the list
        prev = None  # To keep track of the previous node for deletion
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next  # Skip the current node (delete it)
                else:
                    self.table[index] = current.next  # If it's the first node, move head
                return True  # Successfully deleted
            prev = current  # Move to the next node
            current = current.next
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
        self.capacity = capacity  # Maximum capacity of the dictionary
        self.size = 0  # Current size (number of elements)
        self.bucket = self.make_array(self.capacity)  # Create an array for the hash table

    def make_array(self, capacity):
        """Create an empty array with the given capacity."""
        L = []  # Initialize an empty list
        for i in range(capacity):
            L.append(None)  # Append None for each slot in the array
        return L
    