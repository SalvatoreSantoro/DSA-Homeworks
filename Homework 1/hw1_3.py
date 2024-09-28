import heapq

# case = (k, array)
test_cases = [(1,[1]), (2,[3,2,7,6,5]), (4,[10,12,1,2,3,4])]
for case in test_cases:
    k = case[0]
    arr = case[1]
    n = len(arr)
    min_heap = arr[:k+1]
    heapq.heapify(min_heap)

    index = 0
    for i in range(k+1, n):
        min_element = heapq.heappop(min_heap)
        arr[index] = min_element
        index += 1
        heapq.heappush(min_heap, arr[i])
    while min_heap:
        min_element = heapq.heappop(min_heap)
        arr[index] = min_element
        index += 1

    print(arr)

# output atteso:
# [1]
# [2, 3, 5, 6, 7]
# [1, 2, 3, 4, 10, 12]