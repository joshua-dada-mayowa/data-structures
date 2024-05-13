"""
Implementation

* Binary search is a fast search algorithm that finds the presence of a target value within a sorted array.
* Recursive binary search is a variant of binary search that uses recursion to search for the target value.

"""

def recursive_binary_search(arr: list, target: int) -> bool:
    """
    Returns True if the target is found in the array, False otherwise
    """
    # Base case: if the array is empty, the target is not found
    if len(arr) == 0:
        return False
    
    # Recursive case:
    else:
        # Calculate the midpoint index
        midpoint = len(arr) // 2

        # If the target is found at the midpoint, return True
        if arr[midpoint] == target:
            return True
        
        # If the target is greater than the midpoint, search in the right half
        elif arr[midpoint] < target:
            return recursive_binary_search(arr[midpoint + 1:], target)
        
        # If the target is smaller than the midpoint, search in the left half
        else:
            return recursive_binary_search(arr[:midpoint], target)
        

if __name__ == "__main__":
    arr = [2, 3, 4, 5, 6, 6, 7]  # Note: This array is not sorted, binary search requires a sorted array
    target = 10
    result = recursive_binary_search(arr, target)
    print(result)