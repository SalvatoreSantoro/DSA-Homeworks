
def build_max_heap_v2(A):
    heap_size=1
    for i in range(1,len(A)):
        insert(A, A[i], heap_size)
        heap_size += 1

def insert(arr, element, heap_size):
    arr[heap_size] = element
    parent = int((heap_size)/2)

    current = heap_size
    while (arr[current] > arr[parent]):
        (arr[current], arr[parent]) = (arr[parent], arr[current])
        current = parent
        parent = int((current)/2)

test_cases = [[10,12,8], [1,2,3,4,5,6], [10,12,14,3,4,5,1,15]]
for case in test_cases:
    build_max_heap_v2(case)
    print(case)

# output atteso:
# [12, 10, 8]
# [6, 5, 4, 2, 1, 3]
# [15, 14, 10, 12, 4, 5, 1, 3]
    
# La procedura build_max_heap classica e build_max_heap_v2 non generano lo stesso heap a partire da uno stesso array di input.
# Ad esempio:
    
'''
import heapq
a = [10, 12, 14, 3, 4, 5, 1, 15]
heapq._heapify_max(a)
print(a)
# output con build_v2: [15, 14, 10, 12, 4, 5, 1, 3]
# output con build classica: [15, 12, 14, 10, 4, 5, 1, 3]
'''