# Complexity O(n^2)
def moveZeros(arr):
    i=j=0
    length = len(arr)
    print(length)
    for j in range(len(arr)):
        if arr[j] == 0:
            arr.append(0)
    k = 0       
    while (k<length):
        if arr[i] == 0:
            arr.pop(i) # pop has complexity O(n)          
        else:
            i+=1
        k+=1
    return arr

#%%
    # O(n) solution
def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[z] = array[z], array[i]
            print(array)
            z += 1
    return array