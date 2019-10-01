class Node:

    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


def LCAsearch(root, n1, n2):
    if root is None:
        return False;

    if root.key == n1.key or root.key == n2.key:
        return root

    left_lca = LCAsearch(root.left,n1,n2)
    right_lca = LCAsearch(root.right,n1,n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca != None else right_lca

def put(root,key):
    if (root == None):
        return Node(key)

    if (key < root.key) : root.left = put(root.left, key)
    elif key > root.key: root.right = put(root.right, key)


