# 双向链表基础逻辑

class DoublyNode(object):
    def __init__(self, value: object, pre = None, next = None):
        self.value = value
        self.pre = pre
        self.next = next
        
class DoublyLinkedList(object):
    def __init__(self):
        self._head = None
    
    def insert(self, node: DoublyNode) -> bool:
        if self._head is None:
            self._head = node
            return True
        current = self._head
        while current.next:
            current = current.next
        current.next, node.pre = node, current
        return True
    
    def insert_by_index(self, node: DoublyNode, index: int) -> bool:
        if self._head is None:
            if index == 0:
                self._head = node
                return True
            return False
        current = self._head
        while current and index > 1:
            current, index = current.next, index - 1
        if current is None:
            # 越界
            return False
        node.pre, node.next, current.next = current, current.next, node
        return True

    def print(self):
        current, printStr = self._head.next, 'None <-- %s'%(str(self._head.value))
        while current:
            printStr += ' <--> %s'%(str(current.value))
            current = current.next
        print('[%s --> None]'%printStr)

if __name__ == "__main__":
    node1 = DoublyNode(1)
    node2 = DoublyNode(2)
    node3 = DoublyNode(3)
    node4 = DoublyNode(4)

    linkedList = DoublyLinkedList()
    linkedList.insert(node1)
    linkedList.insert(node2)
    linkedList.insert(node4)
    linkedList.insert_by_index(node3, 3)
    linkedList.print()