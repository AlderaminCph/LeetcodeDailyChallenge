import pytest
from problems.two_sum_4_input_is_a_bst import TreeNode, find_target
from typing import List


@pytest.mark.parametrize(
    ["root", "k", "expected_result"],
    [
        ([5, 3, 6, 2, 4, None, 7], 9, True),
        ([5, 3, 6, 2, 4, None, 7], 28, False),
    ],
)
def test_two_sum(root: List[int], k: int, expected_result: bool):
    # create binary tree from list
    bst = TreeNode.to_binary_tree(root)
    assert expected_result == find_target(bst, k)
