def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1 - i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
                
arr = [99,88,77,66,44,22,11]
print(bubble_sort(arr))            