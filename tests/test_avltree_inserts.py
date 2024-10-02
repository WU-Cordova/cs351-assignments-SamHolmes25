import pytest

from datastructures.avltree import AVLTree

class TestAVLInserts():
    @pytest.fixture
    def avltree(self) -> AVLTree: return AVLTree[int, int]([(8, 8), (9, 9), (10, 10), (2, 2), (1, 1), (5, 5), (3, 3), (6, 6), (4, 4), (7, 7)])

    @pytest.fixture
    def small_avltree(self) -> AVLTree: return AVLTree[int, int]([(10,10), (5,5), (20,20), (3,3), (7,7), (15,15), (30,30)])

    def test_insert_empty_tree(self) -> None:
        tree = AVLTree[int, int]()
        tree.insert(1, 1)
        assert tree.inorder() == [1]
    
    def test_insert_existing_key(self, avltree: AVLTree) -> None:
        with pytest.raises(ValueError):
            avltree.insert(8, 8)

    def test_insert_left_child(self, avltree: AVLTree) -> None:
        avltree.insert(0, 0)
        assert avltree.inorder() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_insert_right_child(self, avltree: AVLTree) -> None:
        avltree.insert(11, 11)
        assert avltree.inorder() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 

    def test_insert_left_grandchild(self, avltree: AVLTree) -> None:
        avltree.insert(-1, -1)
        assert avltree.inorder() == [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_insert_right_grandchild(self, avltree: AVLTree) -> None:
        avltree.insert(12, 12)
        assert avltree.inorder() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

    def test_inorder_traversal(self, avltree):
        # Expected inorder traversal result based on the keys in sorted order
        expected_inorder_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Get the actual inorder traversal keys from the AVL tree
        result_keys = list(avltree.inorder())
        
        # Compare the expected and actual results
        assert result_keys == expected_inorder_keys, f"Expected {expected_inorder_keys}, but got {result_keys}"



    def test_postorder_traversal(self, small_avltree):
        # Expected postorder traversal result based on the structure of the AVL tree
        expected_postorder_keys = [3, 7, 5, 15, 30, 20, 10]
        
        # Get the actual postorder traversal keys from the AVL tree
        result_keys = list(small_avltree.postorder())
        
        # Compare the expected and actual results
        assert result_keys == expected_postorder_keys, f"Expected {expected_postorder_keys}, but got {result_keys}"

    def test_preorder_traversal(self, small_avltree):
        # Expected preorder traversal result based on the structure of the AVL tree
        expected_preorder_keys = [10, 5, 3, 7, 20, 15, 30]
        
        # Get the actual preorder traversal keys from the AVL tree
        result_keys = list(small_avltree.preorder())
        
        # Compare the expected and actual results
        assert result_keys == expected_preorder_keys, f"Expected {expected_preorder_keys}, but got {result_keys}"
    
    def test_bforder(self, small_avltree):
        # Expected BFS traversal result based on the structure of the AVL tree
        expected_bfs_keys = [10,5,20,3,7,15,30]
        
        # Get the actual BFS traversal keys from the AVL tree
        result_keys = list(small_avltree.bforder())
        
        # Compare the expected and actual results
        assert result_keys == expected_bfs_keys, f"Expected {expected_bfs_keys}, but got {result_keys}"

    def test_delete(self, small_avltree):
        small_avltree.insert(16, 16)
        small_avltree.delete(10)
        assert small_avltree.bforder() == [15,5,20,3,7,16,30]
    
    def test_size(self, small_avltree):
        assert small_avltree.size() == 7
    
    def test_print(self, avltree):
        assert str(avltree) == "10\n5\n3\n7\n20\n15\n30\n"