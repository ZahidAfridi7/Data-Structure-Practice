class Dictionary:
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def hashFun(self,key):
        return abs(hash(key)) % self.size
        
    def reHash(self,old_hash):
        return (old_hash + 1) % self.size
    
    def __setitem__(self,key,value):
        self.put(key,value)
    
    def get(self,key):
        start_pos = self.hashFun(key)
        current_pos = start_pos
        while self.slots[current_pos] != None:
            if self.slots[current_pos] == key:
                return self.data[current_pos]
            current_pos = self.reHash(current_pos)
            if current_pos == start_pos:
                print ("Not Found")
        print ("Not Found")            
        
    def put(self,key,value):
        hash_value = self.hashFun(key)
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.reHash(hash_value)
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.reHash(new_hash_value)
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value        

d1 = Dictionary(3)
d1.put('c',1100)
d1.put('ja',2000)
d1.put('pyt',1000)
print(d1.slots)
print(d1.data)