# LeetCode 24 Practice

from common.linkedlist import ListNode
from common.printer import printLinkedList

def swap_in_pair(head: ListNode) -> ListNode:
    if head is None:
        return None
    # 运用哨兵Node，为了不丢失最终的Node头节点
    # 如果不适用哨兵，则最后的结果会变成1->4->3->5少了2这个头
    origin = ListNode(0, head)
    pre, current = origin, head
    while current and current.next:
        # 创建两个变量，一个next是为了和current互换，另一个n_next则为了互换之后可以正确地指向next节点
        next, n_next = current.next, current.next.next
        current.next, next.next = n_next, current
        # pre的作用是前置指针，同样也是为了保证前驱节点在互换位置时不丢失
        pre.next = next
        # 最后运算结束后开始向前移位
        pre, current = current, n_next
    return origin.next
            

# Testcase
node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

result = swap_in_pair(node1)
while result:
    print(result.val)
    result = result.next