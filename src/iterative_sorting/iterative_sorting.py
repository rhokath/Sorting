# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
      
        for j in range(cur_index, len(arr) - 1):
            if arr[j + 1] < arr[smallest_index]:
                smallest_index = j + 1
        temp_variable = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp_variable

             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # while a swap happened loop through and compare the element at n and n + 1, if element at n is > n+1 swap the elements
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr)-1):
            
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True 

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr