# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from common.linkedlist import ListNode
from common.printer import printLinkedList

class Solution:
    def reverseList(self, head: ListNode):
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            current, pre = head, None
            while current:
                current.next, pre, current = pre, current, current.next
            return pre

# Testcase
# foo = [1, 2, 3, 4, 5]
# bar = Solution()
# result = bar.reverseList(foo)
# print(result)

# Tips
# 一共有两种解法，一种是循环修改即代码部分，另一种是递归修改