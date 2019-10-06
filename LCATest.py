import unittest
from LCA import Node


class basicTest(unittest.TestCase):
    root = Node(1)

    def rootTest(self):
        root = Node(1)
        self.assertEquals(root.key,1,"Checking if root gets instanciated correctly")

