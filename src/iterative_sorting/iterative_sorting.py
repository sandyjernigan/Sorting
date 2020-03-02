# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        # current index, Start with current index = 0
        cur_index = i
        smallest_index = cur_index

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

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(selection_sort(arr1))


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

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr