# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
from common.linkedlist import ListNode
from common.printer import printLinkedList

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 探路环解法
        if head is None:
            return False
        if head.next is None:
            return False
        slow, fast = head, head
        while slow and fast:
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

# Tips
# 本题有三个解法
# 1、暴力循环方法：在0.5s或者1s内无限后移指针，当指针指向空说明无环否则有环
# 2、hash表解法（142 Cycle II 这个题用了Hash表法）：遍历链表，将每个node存入hash表中，并且对比，如果存在说明有环否则无环 
# 3、快慢指针解法（代码解法）：设置两个指针一个快一个慢，循环链表当两个指针指向同一个node说明有环否则无环