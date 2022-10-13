"""
Given the head of a linked list and an integer val, remove all the nodes of
the linked list that has Node.val == val, and return the new head.



Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
"""
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        dummy_node = ListNode(None, head)
        current_node = head
        prev_node = dummy_node
        while current_node:
            if current_node.val == val:
                current_node.val = current_node.next.val
                current_node.next = current_node.next.next
            prev_node = current_node
            current_node = current_node.next
        return prev_node
