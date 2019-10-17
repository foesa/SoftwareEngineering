class Node:
    def __init__(self, key):
        self.key = key
        self.prev = []
        self.succ = []

def LcaDAG(root, n1, n2):
    if root is None:
        return None
    if root.key == n1.key or root.key == n2.key:
        return root.key
    if n1.key == n2.key:
        return n1.key
    lca = []

    for i in range(len(n1.prev)):
        for j in range(len(n2.prev)):
            if (n1.prev[i].key == n2.prev[j].key):
                lca.append(n1.prev[i].key)

    if (lca == []):
        if (n1.key > n2.key):
            lca.append(LcaDAG(root, n1.prev[0], n2))
        else:
            lca.append(LcaDAG(root, n1, n2.prev[0]))
    return max(lca)