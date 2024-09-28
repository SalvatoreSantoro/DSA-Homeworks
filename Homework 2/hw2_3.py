from math import sqrt

test_cases = [1, 200, 1000]
for n in test_cases:
    DP = [0 for i in range(n+1)]
    parent = {}

    for k in range(1,n+1):
        elem=float("inf")
        argmin = float('inf')
        for rad in range(1, int(sqrt(k)+1)):
            if DP[k-(rad**2)]+1 < elem:
                elem = DP[k-(rad**2)]+1
                argmin = rad
        parent[k] = argmin
        DP[k]=elem

    # parent pointers
    root = n
    st = '('
    while root:
        st += str(parent[root])+'^2 + '
        root = root - parent[root]**2
    print(DP[n])
    print(st[:-3]+')')

# output atteso:
# 1
# (1^2)
# 2
# (2^2 + 14^2)
# 2
# (10^2 + 30^2)