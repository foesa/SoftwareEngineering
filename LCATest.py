import unittest
import LCA as lca


class basicTest(unittest.TestCase):

    def testroot(self):
        root = lca.Node(1)
        self.assertEqual(root.key,1,"Checking if root gets instantiated correctly")
        print("rootTest passed")

    def testPut(self):
        root = lca.Node(7)
        lca.put(root,8)
        lca.put(root,3)
        lca.put(root,1)
        lca.put(root,2)
        lca.put(root,6)
        lca.put(root,4)
        lca.put(root,5)
        tree = lca.inOrderPrint(root,"")
        print(tree)
        self.assertEqual(tree,"12345678","Checking if keys get put into tree correctly")
        print("testPut passed")

    def testisInTree(self):
        root = lca.Node(7)
        lca.put(root, 8)
        lca.put(root, 3)
        lca.put(root, 1)
        lca.put(root, 2)
        lca.put(root, 6)
        lca.put(root, 4)
        lca.put(root, 5)
        self.assertEqual(True,lca.inTree(root,5),"Checking to see if a node is in the tree for lca")
        self.assertEqual(False,lca.inTree(root,0),"If node is not in tree return null")
        print("isInTree passed")

    def testlcaSearch(self):
        root = lca.Node(7)
        lca.put(root, 8)
        lca.put(root, 3)
        lca.put(root, 1)
        lca.put(root, 2)
        lca.put(root, 6)
        lca.put(root, 4)
        lca.put(root, 5)
        self.assertEqual(3,lca.LCAsearch(root,6,1,False).key,"Lca for 2 keys in tree")
        self.assertEqual(False,lca.LCAsearch(root,0,1,False),"If a key is not in tree tree returns false")
        root = None
        self.assertEqual(False,lca.LCAsearch(root,2,1,False),"If root is none will return False")
        print("lcaSearch passed")


if __name__ == '__main__':
    unittest.main()