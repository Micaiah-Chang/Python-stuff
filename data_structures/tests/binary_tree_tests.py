from nose.tools import *
from binary_tree.binary_tree import BinaryNode
from binary_tree.binary_tree import BinaryTree


def test_key_init():
    node = BinaryNode(2,None)
    assert_equal(node._key, 2)
    assert_equal(node.parent, None)
    assert_equal(node.left, None)
    assert_equal(node.right,  None)

def test_key_add():
    node_root =  BinaryNode(2,None)
    node_root.make_left(1)
    node_root.make_right(3)
    assert_equal(node_root.left._key, 1)
    assert_equal(node_root.right._key, 3)
    assert_equal(node_root.left.parent._key, 2)
    assert_equal(node_root.right.parent._key, 2)

def test_tree():
    test_tree = BinaryTree(2)
    test_tree.insert(3)
