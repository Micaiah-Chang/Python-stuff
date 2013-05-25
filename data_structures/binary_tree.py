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
        if value:
            return
        else:
            if new < current._key:
                current.make_left(new)
            elif new > current._key:
                current.make_right(new)

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

    def make_left(self, child):
        self.left = BinaryNode(child, self)

    def make_right(self, child):
        self.right = BinaryNode(child, self)



