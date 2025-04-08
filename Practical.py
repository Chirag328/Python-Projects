# Binary Search
def binary(arr,user):
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == user:
            print(f"Number found at {mid}")
            break 
        elif arr[mid] < user:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print("Element not found")
        
 
 
arr = [1,2,5,7,9,36]
arr.sort()
print(arr)
user = int(input("Enter a number to search: "))
binary(arr,user)

# Bubble sorting
def bubble(arr1):
    length = len(arr1) - 1
    run = 0
    while run < length:
        i = 0
        j = 1
        while j < length:
            if arr1[i] > arr1[j]:
                temp = arr1[j]
                arr1[j] = arr1[i]
                arr1[i] = temp
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        run += 1
    print(f'Sorted list: {arr1}')
    
arr1 = [7,5,2,9,36,1,52,92]
print(f'list: {arr1}')
bubble(arr1)

# Selection sorting
def selction(arr2):
    for i in range(len(arr2)):
        mini = i
        for j in range(i+1,len(arr2)):
            if arr2[j] < arr2[mini]:
                mini = j
        arr2[i],arr2[mini] = arr2[mini],arr2[i]
    print(f'Sorted list: {arr2}')
        
arr2 = [7,5,2,9,36,1,52,92]
print(f'list: {arr2}')
selction(arr2)




