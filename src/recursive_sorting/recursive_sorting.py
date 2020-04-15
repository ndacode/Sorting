# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    print(f" MERGING{arrA} - {arrB}")
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(elements):
       if a >= len(arrA):
           merged_arr[i] = arrB[b]
           b += 1
       elif b >= len(arrB):
           merged_arr[i] = arrA[a]
           a =+1
       elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a+= 1
       else: 
            merged_arr[i] = arrB[b]
            b+=1
    return merged_arr

arr = [3,7,5,4,8,50,2,6,80]
# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    print(f"SORTING {arr}")
    if len(arr) <= 1:
        return arr
    split = len(arr)//2
    left = arr[:split] 
    right = arr[split:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
        

#  Time complexity of merge_sort is O(n log n)   
#  log is a recursive reduction of the number of passes over n?  

merge_sort(arr)

   
# split the array in half
# split the array in half again
# sort each array
# then merge them

    # return arr

print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
