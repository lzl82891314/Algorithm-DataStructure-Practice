# 趁热打铁练习分组反转
# 逻辑：通过两个指针，一个探路，一个做反转操作

from common.linkedlist import ListNode
from common.printer import printLinkedList

def reverse_in_k(head: ListNode, k: int):
    if head is None:
        return None
    if head.next is None:
        return head
    if k <= 1:
        return head
    
    origin = ListNode()
    flag, fast, slow, count, is_first = False, head, head, k, True
    while fast:
        while fast and count > 0:
            fast, count = fast.next, count - 1
        if count > 0 or fast is None:
            break
        if is_first:
            pre = fast
            is_first = False
        else:
            pre = slow
        current, count = slow, k
        while count > 0:
            # current.next, pre.next, current.next.next, current, pre, count = current.next.next, current, current, current.next, current, count - 1
            current.next, pre, current = pre, current, current.next
            count = count - 1
        if not flag:
            origin.next = pre
        slow, count = fast, k
    return origin.next

# Testcase
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
result = reverse_in_k(node1, 2)
while result:
    print (result.val)
    result = result.next
    
        