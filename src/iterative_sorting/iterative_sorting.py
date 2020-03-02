# Selection Sort function
def selection_sort( arr ):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        # current index, Start with current index = 0
        smallest_index = i

        # Loop through elements on right-hand-side of current index and find the smallest element
        for j in range(i+1, len(arr)):

            # if element at j index is smaller
            if arr[j] < arr[smallest_index]:
                # update smallest index to location in j loop 
                smallest_index = j

        # Swap the element at current index with the smallest element found in above loop
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    # Return Sorted Array
    return arr


# Bubble Sort function
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

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr