# 反转链表反复练习
from common.linkedlist import ListNode
from common.printer import printLinkedList

def reverseLinkedlist(head: ListNode) -> ListNode:
    # 首先参数检测
    if head is None:
        return None
    if head.next is None:
        return head
    
    # 开始执行反转链表操作
    # 方法：使用前继指针和当前指针共同判定
    pre, current = None, head
    while current:
        # python 独有写法，python中下段赋值操作会全部同时执行，省去了中间变量
        current.next, pre, current = pre, current, current.next
        
        # 写法二，通用写法，创建变量赋值
        # temp = current.next
        # current.next = pre
        # pre = current
        # current = temp
    return pre

# Testcase
node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)

print('before head: ')
printLinkedList(head)
print('after head: ')
result = reverseLinkedlist(head)
printLinkedList(result)