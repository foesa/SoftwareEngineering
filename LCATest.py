import unittest
import LCA as lca


class basicTest(unittest.TestCase):
    root = lca.Node(1)

    def rootTest(self):
        root = lca.Node(1)
        self.assertEquals(root.key,1,"Checking if root gets instantiated correctly")

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
        self.assertEqual(tree,"1 2 3 4 5 6 7 8","Checking if keys get put into tree correctly")

    def isInTree(self):
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
