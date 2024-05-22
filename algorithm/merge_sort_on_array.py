def split(arr):
    """
    Divides the unsorted list at midpoint into sublists 
    Return two sublists - left and right 
    Takes O(log n) time"""
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return left,right

def merge_sort(left,right):
    """
    Merges two list, sorting them in the process 
    Returns a new merged list
    Takes O(n) Time"""

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
            l.append(left[i])
            i += 1
    while j < len(right):
            l.append(right[j])
            j += 1
    return l

def recursive_merge_sort(arr):
    """
    Implementation of 
    Merge sort on an array"""

    if len(arr) <= 1:
        return arr
    
    left_half, right_half = split(arr)
    left = recursive_merge_sort(left_half)
    right = recursive_merge_sort(right_half)

    return merge_sort(left, right)


if __name__ == "__main__":
    arr = [21,20,5,60,7] 
    result = recursive_merge_sort(arr)
    print(result)