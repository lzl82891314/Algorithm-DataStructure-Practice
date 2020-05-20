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
        
        
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        
        pre, current = None, head
        while current:
            # swap
            current.next, pre, current = pre, current, current.next
        return pre
        

# Testcase
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
foo = Solution()
# result = foo.reverseLinkedList(node1)
# while result:
#     print(result.val)
#     result = result.next
result = foo.reverseLinkedList(node1)
while result:
    print (result.val)
    result = result.next