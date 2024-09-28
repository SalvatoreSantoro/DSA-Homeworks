class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val <= key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

test_cases = [[2], [5,2,1,4], [3,1,5,8,9,10,2,7,6,4]]
for case in test_cases:
    root = None
    for elem in case:
        root = insert(root, elem)
    inorder(root)
    print('')

# output atteso:
# 2 
# 1 2 4 5
# 1 2 3 4 5 6 7 8 9 10
