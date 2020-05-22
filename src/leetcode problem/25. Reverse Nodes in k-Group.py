# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
from common.linkedlist import ListNode
from common.printer import printLinkedList

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or k == 1:
            return head
        if head is None:
            return None
        if head.next is None:
            return head
        origin, slow, fast, count = self, head, head, k
        while fast:
            while fast and count > 0:
                fast, count = fast.next, count - 1
            if count > 0:
                break
            
            origin.next = self.inner_reverse(slow, fast, k)
            temp = k
            while temp:
                origin, temp = origin.next, temp - 1
            slow, count = fast, k
        return self.next
        
        
    def inner_reverse(self, head: ListNode, next: ListNode, deep: int) -> ListNode:
        pre, current = next, head
        while deep:
            # swap
            current.next, pre, current, deep = pre, current, current.next, deep - 1
        return pre
        

# Testcase
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
foo = Solution()
result = foo.reverseKGroup(node1, 3)
while result:
    print (result.val)
    result = result.next