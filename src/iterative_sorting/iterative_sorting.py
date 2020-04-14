# TO-DO: Complete the selection_sort() function below 


numbahs = [23, 53, 90, 254, 34, 36, 3, 78, 67, 70, 94]

def selection_sort( numbahs ):
    print(f'selection_sort: {numbahs}')
    # loop through n-1 elements
    for i in range(0, len(numbahs)):
        temp = numbahs[i]    
        j = i
        while j > 0 and temp < numbahs[j-1]:
            numbahs[j] = numbahs[j - 1]
            j-=1
            numbahs[j] = temp
    print (f'selection_sort: {numbahs}')
    return numbahs

selection_sort(numbahs)


      
numbahs = [23, 53, 90, 254, 34, 36, 3, 78, 67, 70, 94]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( numbas ):
    print(f'bubble_sort: {numbahs}')
    for num in numbahs: 
        for i in range(0, len(numbahs)-1):
            if numbahs[i] > numbahs[i+1]:
                numbahs[i], numbahs[i +1] = numbahs[i + 1], numbahs[i]
             
    print(f'bubble_sort: {numbahs}')

bubble_sort(numbahs)

# compare the first two indices of an array
# if the higher index is larger than the lower index, swap them
# move to the next pair of indices and repeat that action


    # return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr