"""
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.



Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        while current_node:
            while (
                current_node.next and current_node.val == current_node.next.val
            ):
                current_node.next = current_node.next.next
            current_node = current_node.next
        return head
