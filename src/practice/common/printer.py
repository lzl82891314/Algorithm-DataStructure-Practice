from .linkedlist import ListNode

def printLinkedList(head: ListNode):
    if head is None:
        print ('[]')
    if head.next is None:
        print('[%d]' %head.val)
    nodeStr, current = '%d'%head.val, head.next

    while current:
        nodeStr += ' --> %d'%current.val
        current = current.next
    nodeStr += ' --> None'
    print('[%s]'%nodeStr)