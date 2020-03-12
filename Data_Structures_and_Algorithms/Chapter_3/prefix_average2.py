def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]"""
    n = len(S)
    A = [0] * n # Create new list of n zeros
    for j in range(n): # O(n^2)
        A[j] = sum(S[0J+1]) / (j+1) # Record the average
    return A

    # O(n^2)