# Complexity O(n^2)
def maxSubArray(arr):
    array_sum = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            array_sum.append(sum(arr[i:j+1]))
            print(array_sum)
    return max(array_sum)

#%%
# Efficient approach with Kadane's algorithm, O(n) solution
def maxSubArray(arr):
    max_arr = maximum = arr[0];
    for i in range(1,len(arr)):
        max_arr = max(arr[i], max_arr+arr[i])
        maximum = max(max_arr, maximum)
    return maximum