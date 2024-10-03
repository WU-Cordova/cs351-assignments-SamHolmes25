import pytest
from datastructures.avltree import AVLTree

class TestCopyMethods:

    def test_insert_when_empty(self):
        # Arrange (set up your test data)
        avl_tree = AVLTree()

        # Act (perform the action you want to test)
        avl_tree.insert(10, 'ten')

        # Assert (check that the test is passing)
        assert avl_tree.root.key == 10
        assert avl_tree.root.value == 'ten'
        assert avl_tree.root.height == 0
    
    def test_insert_when_not_empty(self):
        # Arrange (set up your test data)
        avl_tree = AVLTree()
        avl_tree.insert(10, 'ten')

        # Act (perform the action you want to test)
        avl_tree.insert(20, 'twenty')
        avl_tree.insert(5, 'thirty')

        # Assert (check that the test is passing)
        assert avl_tree.root.key == 10
        assert avl_tree.root.value == 'ten'
        assert avl_tree.root.height == 1
        assert avl_tree.root.right.key == 20
        assert avl_tree.root.right.value == 'twenty'
        assert avl_tree.root.right.height == 0
        assert avl_tree.root.left.key == 5
        assert avl_tree.root.left.value == 'thirty'
        assert avl_tree.root.left.height == 0
    
    def test_insert_left_rotation(self):
        # Arrange (set up your test data)
        avl_tree = AVLTree()
        avl_tree.insert(30, 'thirty')
        avl_tree.insert(20, 20)
        avl_tree.insert(10, 10)
        #avl_tree.insert(30, 30)

        assert avl_tree.root.key == 20

    def test_insert_right_rotation(self):
        # Arrange (set up your test data)
        avl_tree = AVLTree()
        avl_tree.insert(10, 'ten')
        avl_tree.insert(20, 'twenty')
        avl_tree.insert(30, 'thirty')
        #avl_tree.insert(30, 30)

        assert avl_tree.root.key == 20