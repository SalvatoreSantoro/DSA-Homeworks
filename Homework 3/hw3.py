'''
memo = {}
def DP(i,s):
    if (i,s) in memo:
        return memo[(i,s)]
    if i == len(G) or s == size:
        return 0
    memo[(i,s)] = max(1+DP(i+1,s+G[i]) if s+G[i] <= size else float('-inf'), DP(i+1,s))
    return memo[(i,s)]
'''

def greedy(G):
    G.sort()
    sum = 0
    i = 0
    while (sum + G[i] <= size):
        sum += G[i]
        i +=1
    return i

# ogni case è una tupla contenente la capacità dello stadio e l'array di gruppi
test_cases = [(10,[8,2,2,5,9,3]), (50,[40,20,20,30]), (100,[20,30,25,5,35,30,20])]
for case in test_cases:
    size = case[0]
    G = case[1]
    print(greedy(G))
    #memo.clear()
    #print('dp: ', DP(0,0))

# output atteso:
# 3
# 2
# 5