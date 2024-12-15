import random

def monkey_sort(arr):
    while arr != sorted(arr):
        random.shuffle(arr)
        print(arr)
    print(arr)
a = [11111,22,111,222,3333,111111,33333,1]

monkey_sort(a)        
        