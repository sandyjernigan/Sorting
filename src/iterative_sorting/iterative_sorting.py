# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # Loop through your array
    for i in range(len(arr)):

        # Boolean to test if swap was required 
        swap = False

        # Compare each element to its neighbor
        for j in range(0, len(arr)-1-i):

            # If elements in wrong position (relative to each other, swap them)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # swap was required = True
                swap = True

        # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
        if swap == False:
            break

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr