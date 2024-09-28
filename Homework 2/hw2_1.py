
def update_memo(A, k):
    global memo
    for i in range(len(A)-1,-1,-1):
        x,y = A[i]
        if(memo[x][y]<k+len(A)-i):
            memo[x][y] = k + len(A) - i
        else:
            break

def process_solution(A, k):
    global maximum
    maximum = max(maximum, k+len(A))
    update_memo(A, k)

def get_candidates(A):
    candidates = []
    x,y = A[-1]
    for ofx,ofy in directions:
        if (0 <= x+ofx < N) and (0 <= y+ofy < M):
            if input[x+ofx][y+ofy] > input[x][y]:
                candidates.append((x+ofx, y+ofy))
    return candidates

def backtracking(A):
    x,y = A[-1]
    k = memo[x][y]                              # k = valore della sottosoluzione per la cella gia' visitata
    if k != 0:                                  # terminazione per cella gia' visitata (pruning)
        process_solution(A[:-1], k)             # ultimo elemento escluso perche' gia' visitato
        return
    candidates = get_candidates(A)
    if not candidates:                              # terminazione della sequenza crescente (candidates = vuoto)
        process_solution(A, 0)
        return
    for c in candidates:
        A.append(c)
        backtracking(A)
        A.pop()

directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
test_cases = [
[[5]],
[[3,4,5],
 [2,1,6],
 [1,6,12]],
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], 
 [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
 [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
 [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
]

for input in test_cases:
    maximum = 0
    N = len(input)
    M = len(input[0])
    memo = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            backtracking([(i,j)])
    print(maximum)

# output atteso:
# 1
# 7
# 50
