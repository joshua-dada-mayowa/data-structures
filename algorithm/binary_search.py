"""
Implementation 

* Binary search is a fast search algorithm that finds the position of a target value within a sorted array.
* It compares the target value to the middle element of the array and eliminates half of the array for each iteration.

"""
def binary_search(arr: list, target: int):
    """
    Returns the index position of target if found else returns None
    """
    # Initialize the first and last indices
    first = 0
    last = len(arr) - 1

    # Iterate through the list until the target is found or the search space is exhausted
    while first <= last:
        # Calculate the midpoint index
        midpoint = (first + last) // 2

        # Check if the value at the midpoint is equal to the target value
        if arr[midpoint] == target:
            return midpoint
        # If the target is greater, move the first index to the right of the midpoint
        elif arr[midpoint] < target:
            first = midpoint + 1
        # If the target is smaller, move the last index to the left of the midpoint
        else:
            last = midpoint - 1

    # Return None if the target is not found
    return None

if __name__ == "__main__":
    arr=[2,3,4,5,6,6,7] 
    target=4
    result=binary_search(arr,target)
    print(result)