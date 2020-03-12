def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]"""
    n = len(S) # O(1)
    A = [0] * n # Create new list of n zeros, O(n)
    total = 0 # Compute prefix sum as S[0] + S[1] + ...
    for j in range(n): # O(n)
        total += S[j] # Update prefix sum to include S[j], O(n)
        A[j] = total / (j+1) # Compute average based on current sum, O(n)
    return A

    #O(n)