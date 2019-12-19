import unittest
from LCADAG.LcaDAG import Node,LcaDAG

class testing(unittest.TestCase):
    def test_simple(self):
        root = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        root.succ = [n2, n3, n4, n5]
        n2.succ = [n4]
        n2.prev = [root]
        n3.succ = [n4, n5]
        n3.prev = [root]
        n4.succ = [n5]
        n4.prev = [n2, n3, root]
        n5.prev = [n3, n4, root]
        n6.prev = [n4]
        lca = LcaDAG(root, n4, n5)
        self.assertEquals(lca,3)

    def test_null(self):
        root = None

        lca = LcaDAG(root, 4, 5)
        self.assertEquals(lca,None)

    def test_root(self):
        root = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        root.succ = [n2, n3]

        lca = LcaDAG(root, root, n3)
        self.assertEquals(lca, 1)
        lca = LcaDAG(root, n3, root)
        self.assertEquals(lca, 1)
        lca = LcaDAG(root, n2, n2)
        self.assertEquals(lca, 2)

    def test_no_immediate_lca(self):
        root = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        root.succ = [n2, n3]
        n2.succ = [n4]
        n2.pred = [root]
        n3.succ = [n4, n5]
        n3.pred = [root]
        n4.succ = [n5]
        n4.pred = [n2]
        n5.pred = [n3]
        n6.pred = [n4]

        lca = LcaDAG(root, n4, n5)
        self.assertEquals(lca, 1)

if __name__ == '__main__':
    unittest.main()