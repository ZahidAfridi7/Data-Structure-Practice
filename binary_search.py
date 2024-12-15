def binary_search(arr,low_index,high_index,item):
    if low_index <= high_index:
        mid = int((low_index + high_index)//2)
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr,low_index,mid-1,item)
        else:
            return binary_search(arr,mid+1,high_index,item)
    return "not found" 
arr = [11,22,33,44,55,66,44,56,77,1000]
print(binary_search(arr,0,len(arr)-1,22))   
print(len(arr))