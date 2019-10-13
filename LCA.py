class Node:

    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class AcyclicNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        #Need more info on DAG to proceed


def LCAsearch(root, n1, n2,bool):
    if (bool == False):
        if (inTree(root,n1) and inTree(root,n2)):
            bool = True
        else :
            return False
    if root is None:
        return False

    if root.key == n1 or root.key == n2:
        return root

    left_lca = LCAsearch(root.left,n1,n2,bool)
    right_lca = LCAsearch(root.right,n1,n2,bool)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca != None else right_lca

def put(root,key):
    if (root == None):
        return Node(key)

    if (key < root.key) : root.left = put(root.left, key)
    elif key > root.key: root.right = put(root.right, key)
    else: root.key = key
    return root
def inTree(root, key):
    if root == None:
        return False

    if root.key == key:
        return True

    if (inTree(root.left, key) or inTree(root.right, key)):
        return True

    return False

def inOrderPrint(root,res):
    if root == None:
        return ""
    else:
        res = inOrderPrint(root.left,res) + str(root.key) + inOrderPrint(root.right,res)
        return res

def acyclicGraphBuilder(root,res):