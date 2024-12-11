import ctypes
    #ctypes are the datatype of c-language used in python

    #step_1 creating list(dynamic array)
class My_list:
            def __init__(self):
                self.size = 1
                self.n = 0
                self.A = self.__make_array(self.size)

    #step_2 Adding Length of Array function len()    
            def __len__(self):
                return self.n    
 
            def append(self, item):
             if self.n == self.size:  # Resize if needed
              self.__resize(self.size * 2)
        # Add the new item
             self.A[self.n] = item
             self.n += 1  # Increment the count of elements

    # Resize the array
            def __resize(self, new_capacity):
               b = self.__make_array(new_capacity)  # Create a new array
               self.size = new_capacity
        # Copy contents of old array into new array
               for i in range(self.n):
                b[i] = self.A[i]
               self.A = b

#step_3 print function
            def __str__(self):
                result = ''
                for i in range(self.n):
                    result = result + str(self.A[i]) + ','
                return '[' + result[:-1] + ']' 
#step_3 Indexing

            def __getitem__(self,index):
                if 0 <= index < self.n:
                    
                    return self.A[index]                 
                else:
                    return "index error"

#step_5 pop
            def pop(self):
                if self.n == 0:
                    return "empty list"
                print(self.A(self.n-1))
                self.n = self.n - 1
#step_6 clear
            def clear(self):
                self.n = 0
                self.size = 1    

#step_7 find
            def find(self,item):
                
               for i in range(self.n):
                if self.A[i] == item:
                    return i
               return "not found"
#step_7 Inserting
            def insert(self,pos,item):
                if self.n == self.size:
                    self.__resize(self.size*2)
                for i in range(self.n,pos,-1):
                    self.A[i] = self.A[i-1]
                self.A[pos] = item
                self.n = self.n + 1    
#step_8 delete item
             
            def __delitem__(self,pos):
                if 0 <= pos < self.n:
                    
                  for i in range(pos,self.n-1):
                    self.A[i] = self.A[i+1]
                self.n = self.n - 1    

#step_9 Remove

            def remove(self,item):
                pos = self.find(item)
                if type(pos) == int:
                    self.__delitem__(pos)
                else:
                    return pos
                
#min/max num                
            def min(self):
                if self.n == 0:
                    return "list empty"
                minimum = 0
                for i in range(1,self.n):
                    if self.A[i] < minimum:
                        minimum = self.A[i]
                return minimum
            def max(self):
                if self.n == 0:
                    return "empty list"           
                maximun = 0
                for i in range(1,self.n):
                    if self.A[i] > maximun:
                        maximun = self.A[i]
                return maximun           
                                   
            def __make_array(self,capacity):
              return (capacity*ctypes.py_object)()
          
          
l = My_list()
l.append(1)
l.append(11)
l.append(50)
l.insert(0,0)
l.append(20)
l.append(70)
print("max: ",l.max())
print("min: ",l.min())
