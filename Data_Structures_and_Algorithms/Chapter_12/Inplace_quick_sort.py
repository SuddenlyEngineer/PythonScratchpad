def inplace_quick_sort(S, a, b):
    '''Sort the list from S[a] ot S[b] inclusive using the quick-sort algorithm.'''
    if a >= b: return # Range is trivially sorted.
    pivot = S[b] # Last element of range is pivot
    left = a # Will scan rightward
    right = b # Will scan leftward
    while left <= right: # Scan until reaching value equal or larger than pivot or right marker
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]: # Scan until reaching value equal or smaller than pivot or left marker
            right -= 1
        if left <= right: # Scans did not strictly cross
            S[left], S[right] = S[right], S[left] # Swap values
            left, right = left + 1, right - 1 # Shrink range
    S[left], S[right] = S[right], S[left] # Put pivot into its final place, currently marked by left marker
    inplace_quick_sort(S, a, left - 1) # Make recursive calls
    inplace_quick_sort(S, left + 1, b)