"""
Implementation of Selection sort
"""
def selection_sort(arr):
    n = len(arr)
    #move through the unsored part of the array
    for i in range(n - 1):
        # Assume the first element is the minimum
        min_index = i
        # Check the rest of the array to find the true minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                # Found a new minimum, remember its  index
                min_index = j
        
        # Swap the minimum element with the first element of the the unsorted section
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

if __name__ == "__main__":
    arr = [568,789,3,90,45,30,19,1] 
    result = selection_sort(arr)
    print(result)