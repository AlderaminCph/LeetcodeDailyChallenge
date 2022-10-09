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

    def to_binary_tree(items: List[int]):
        """Create BT from list of values."""
        n = len(items)
        if n == 0:
            return None

        def inner(index: int = 0) -> TreeNode:
            """Closure function using recursion bo build tree"""
            if n <= index or items[index] is None:
                return None

            node = TreeNode(items[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

            return inner()

    def create_list(tree, templist=[]):
        """
        >>> tree = TreeNode(2, TreeNode(29, TreeNode(26)),\
        TreeNode(4, None, TreeNode(2, TreeNode(9))))
        >>> TreeNode.create_list(tree)
        [2, 29, 4, 26, None, None, 2, None, None, \
None, None, None, None, 9, None]
        """
        items = []
        queue = [tree]

        while queue:
            copy = queue[:]
            queue = []

            for item in copy:
                if item is None:
                    items.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    items.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)

            if all((x is None for x in queue)):
                break
        if items[-1] is None:
            items = items[:-1]
        return items


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


def find_target(root: Optional[TreeNode], k: int) -> bool:
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
