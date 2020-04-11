def find_brute(T, P):
    '''Return the lowest index of T at which substring P begins (or else -1).'''
    n, m = len(T), len(P) # Introduce conveinient notations
    for i in range(n-m+1): # Try every potential starting index within T
        k = 0 # An index into pattern P
        while k < m and T[i+k] == P[k]: # kth character of P matches
            k += 1
        if k == m: # If we reached the end of the patern,
            return i # substring T[i+m] matches P
    return -1 # Failed to find a match starting with any i