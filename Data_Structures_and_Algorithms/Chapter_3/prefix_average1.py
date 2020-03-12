def prefix_average1(S):
    '''Return list such that, for all j, A[j] equals average of S[0], ..., S[j].'''
    n = len(S) # Constant time
    A=[0] * n # O(n)
    for j in range(n): # O(n)
        total = 0
        for i in range(j + 1): # O(n^2)
            total += S[i]
        A[j] = total / (j + 1)
    return A

# O(n) + O(n) + O(n^2) = O(n^2)