def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return "not Found in array"

arr = [11,222,33,44,55]

print(linear_search(arr,55))
