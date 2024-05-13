""" Implementation of linear search algorithm
1. Approach

* Iterate over the list 
* For each value in the list determine if it matches the the target value, if true return the index value
* Return none if index value not found

"""

def linear_search(arr: list, target: int):
    """
    Returns the index position of target if found else returns None
    """
    # Iterate through the list one element at a time
    for i in range(len(arr)):
        # Check if the current element matches the target value
        if arr[i] == target:
            # Return the index position of the target value
            return i

    # Return None if the target value is not found in the list
    return None

if __name__ == "__main__":
    arr=[2,3,4,5,6,6,7] 
    target=4
    result=linear_search(arr,target)
    print(result)

