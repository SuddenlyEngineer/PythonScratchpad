def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high], inclusive."""

    if low > high:
        return False # Interval empty, no match
    else:
        mid = (low + high) // 2 # Integer division
        if target == data[mid]:
            return True # Found a match
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1) # Recur on the portion left of the middle
        else:
            return binary_search(data, target, mid + 1, high) # Recur on the portion right of the middle