class BinaryTree(object):
    """Naive implementation of an unbalanced binary search tree. This is really bad."""
    def __init__(self, root):
        self.root = BinaryNode(root, None)
        # Root

    def search(self, key):
        current = self.root

        while current.left != None or current.right != None:
            if key < current._key:
                current = current.left
            elif key > current._key:
                current = current.right
            elif key == current._key:
                return True, current
      return False, current

    def insert(self, new):
        value, current = self.search(new)
        print value, current
        if value:
            return
        else:
            print "Hi"
            if new < current._key:
                current.left_child(key)
            elif new > current._key:
                current.right_child(key)


    def deletion(self, remove):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass

    def find_predecessor(self, key):
        pass

    def rank(self, key):
        pass

class BinaryNode(object):
    """Helper class that implements nodes"""
    def __init__(self, key, parent):
        self._key = key
        self.parent = parent
        self.left = None
        self.right = None
        # Key should never be mutated

    def left_child(self, child):
        self.left = BinaryNode(child, self)

    def right_child(self, child):
        self.right = BinaryNode(child, self)


from nose import *

test_tree = BinaryTree(2)
test_tree.insert(3)
print test_tree.root.right
