### Complexity O(n1*n2)
arr2 = [1,2,3]
arr1 = [3,4,8,9]

l1 = len(arr1)
l2 =len(arr2)
merged_list = []
a=b=0
if l1 >= l2:
    for i in range(0,l1):
        l2 = len(arr2)
        if l2==0:
            merged_list.extend(arr1)
            break;
        for j in range(0,l2):
            if (arr1[i] < arr2[j-a]):
                merged_list.append(arr1[i]);
                arr1.remove(arr1[i])
                a+=1
                b=a
                break;
            else:
                merged_list.append(arr2[j-b]);
                arr2.remove(arr2[j-b])
                b+=1
                a=b
else:
    for i in range(0,l2):
        l1 = len(arr1)
        if l1==0:
            merged_list.extend(arr2)
            break;
        else: 
            for j in range(l1):
                if (arr2[i] < arr1[j-a]):
                    merged_list.append(arr2[i]);
                    arr2.remove(arr2[i])
                    a+=1
                    b=a
                    break;
                else:
                    merged_list.append(arr1[j-b]);
                    arr1.remove(arr1[j-b])
                    b+=1
                    a=b
print(merged_list)

#%%

# O(n) solution 
def merge_sorted_array(arr1,arr2):
    current_item_arr1 = arr1[0]
    current_item_arr2 = arr2[0]
    merged_array = []
    first_index_arr1 = 0
    first_index_arr2 = 0
    flag = 0
    while (((first_index_arr1 < len(arr1)) or (first_index_arr2 < len(arr2))) and flag == 0):
        if (current_item_arr1 < current_item_arr2):
            merged_array.append(current_item_arr1)
            first_index_arr1 +=1
            if first_index_arr1 >= len(arr1):
                flag = 1
            else:
                current_item_arr1 = arr1[first_index_arr1]
        else:
            merged_array.append(current_item_arr2)
            first_index_arr2 +=1
            if first_index_arr2>= len(arr2):
                flag = 1
            else:
                current_item_arr2 = arr2[first_index_arr2]         
    return merged_array+arr1[first_index_arr1:]+arr2[first_index_arr2:]