import unittest


class basicTest(unittest.TestCase):

    def testroot(self):
        root = LCA.Node(1)
        self.assertEqual(root.key,1,"Checking if root gets instantiated correctly")
        print("rootTest passed")

    def testPut(self):
        root = LCA.Node(7)
        LCA.put(root, 8)
        LCA.put(root, 3)
        LCA.put(root, 1)
        LCA.put(root, 2)
        LCA.put(root, 6)
        LCA.put(root, 4)
        LCA.put(root, 5)
        tree = LCA.inOrderPrint(root, "")
        print(tree)
        self.assertEqual(tree,"12345678","Checking if keys get put into tree correctly")
        print("testPut passed")

    def testisInTree(self):
        root = LCA.Node(7)
        LCA.put(root, 8)
        LCA.put(root, 3)
        LCA.put(root, 1)
        LCA.put(root, 2)
        LCA.put(root, 6)
        LCA.put(root, 4)
        LCA.put(root, 5)
        self.assertEqual(True, LCA.inTree(root, 5), "Checking to see if a node is in the tree for lca")
        self.assertEqual(False, LCA.inTree(root, 0), "If node is not in tree return null")
        print("isInTree passed")

    def testlcaSearch(self):
        root = LCA.Node(7)
        LCA.put(root, 8)
        LCA.put(root, 3)
        LCA.put(root, 1)
        LCA.put(root, 2)
        LCA.put(root, 6)
        LCA.put(root, 4)
        LCA.put(root, 5)
        self.assertEqual(3, LCA.LCAsearch(root, 6, 1, False).key, "Lca for 2 keys in tree")
        self.assertEqual(False, LCA.LCAsearch(root, 0, 1, False), "If a key is not in tree tree returns false")
        root = None
        self.assertEqual(False, LCA.LCAsearch(root, 2, 1, False), "If root is none will return False")
        print("lcaSearch passed")


if __name__ == '__main__':
    unittest.main()