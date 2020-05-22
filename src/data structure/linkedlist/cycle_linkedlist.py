# 循环链表基础逻辑

class CycleNode(object):
    def __init__(self, value: object):
        self.value = value
        self.next = self

class CycleLinkedList(object):
    def __init__(self):
        self._head = None
    
    def insert(self, node: CycleNode) -> bool:
        if self._head is None:
            self._head = node
            self._head.next = self._head
            return True
        current = self._head
        while current.next != self._head:
            current = current.next
        current.next, node.next = node, self._head
        return True
    
    def insert_by_index(self, node: CycleNode, index: int) -> bool:
        if self._head is None:
            if index == 0:
                self._head, node.next = node, self._head
                return True
            return False
        current = self._head
        while index > 1 and current.next != self._head:
            current, index = current.next, index - 1
        if current.next == self._head and index > 1:
            return False
        current.next, node.next = node, self._head
        return True
    
    def print(self):
        current, printStr = self._head.next, '%s'%(str(self._head.value))
        while current != self._head:
            printStr += ' --> %s'%(str(current.value))
            current = current.next
        print('[%s --> %s]'%(printStr, str(self._head.value)))

if __name__ == "__main__":
    node1 = CycleNode(1)
    node2 = CycleNode(2)
    node3 = CycleNode(3)
    node4 = CycleNode(4)

    linkedList = CycleLinkedList()
    linkedList.insert(node1)
    linkedList.insert(node2)
    linkedList.insert(node4)
    linkedList.insert_by_index(node3, 3)
    linkedList.print()
                
        