
def DP(i):
    if i in memo:
        return memo[i]
    if i == len(input)-1:
        return input[i]
    maximum = input[i]
    for j in range(i+1,len(input)):
        if input[j] > input[i]:
            maximum = max(maximum,DP(j)+input[i])
    memo[i] = maximum
    return maximum

test_cases = [[7], [6,1,2,3,4], [5,6,5,1,2,5,7,8,4,4]]
for input in test_cases:
    N = len(input)
    memo = {}
    output = 0
    for i in range(N):                  
        output = max(output, DP(i))         # extra time
    print(output)

# output atteso:
# 7
# 10
# 26
    
