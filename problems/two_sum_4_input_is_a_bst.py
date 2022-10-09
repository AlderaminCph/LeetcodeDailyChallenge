"""
Given the root of a Binary Search Tree and a target number k, return true if
there exist two elements in the BST such that their sum is equal to the given
target.

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

"""
from typing import Optional, List


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Convert Binary Search Tree to an ascending order integer array.
    """
    array = []
    if not root:
        return array
    inorder(root.left)
    array.append(root.val)
    inorder(root.right)


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    """
    Return True if there exist two elements in the BST such that their sum is
    equal to the given target.
    """
    array = inorder(root)  # sorted array
    left, right = 0, len(array) - 1  # apply 2 pointer approach

    while left < right:
        two_sum = array[left] + array[right]
        if two_sum > k:
            right -= 1
        elif two_sum < k:
            left += 1
        else:
            return True
        return False
