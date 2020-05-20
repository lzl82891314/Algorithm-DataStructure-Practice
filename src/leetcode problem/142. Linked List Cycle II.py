# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
from common.linkedlist import ListNode
from common.printer import printLinkedList

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return None
        hash, pointer, index = dict(), head, 0
        while pointer:
            if pointer in hash:
                return pointer
            hash[pointer] = index
            index += 1
            pointer = pointer.next

# Tips
# 此题同上一题141，用到了141没用到的hash表解法，当然也可以使用快慢指针