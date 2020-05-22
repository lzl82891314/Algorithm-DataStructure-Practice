# 自定义一个简单链表链表结构
# 2020-05-21 Update: 做法修改，之前的做法错了，只使用了一个类来完成所有的链表操作，导致了一个问题
# 当需要对头指针即self进行操作的时候，链表中的数据就乱了，因此需要修改使用两个类，一个Node类只当Node节点使用
# 另一个LinkedList类设置一个head指针指向一个Node

class Node(object):
    def __init__(self, value: object, next = None):
        self.value = value
        self.next = next
    
    def print(self):
        current, printStr = self.next, '%s'%(str(self.value))
        while current:
            printStr += ' --> %s'%(str(current.value))
            current = current.next
        print('[%s --> None]'%printStr)

class LinkedList(object):
    def __init__(self, head: Node = None):
        self._head = head
        self._tail = head

    def find_tail(self) -> Node:
        return self._tail
    
    def find_by_index(self, index: int = 0) -> Node:
        current = self._head
        while current and index > 0:
            current, index = current.next, index - 1
        return current
        

    def find_by_value(self, value: object) -> Node:
        current = self._head
        while current and current.value != value:
            current = current.next
        return current
    
    def insert(self, node: Node) -> bool:
        if self._head is None:
            self._head, self._tail = node, node
            return True
        self._tail.next = node
        self._tail = self._tail.next
        return True
    
    def insert_by_index(self, node, index: int = 0) -> bool:
        if node is None:
            return False
        if index == 0:
            # 插入头部
            node.next, self._head = self._head, node
            return True
        current = self._head
        # 注意此处是需要找到插入index的前一个Node节点，因此index需要设置 > 1
        while index > 1 and current:
            current, index = current.next, index - 1
        if current is None:
            # 越界
            return False
        node.next, current.next = current.next, node
        if current == self._tail:
            self._tail = current.next
        return True
    
    def delete_by_index(self, index: int = 0) -> bool:
        if self._head is None:
            # 异常验证
            return False
        # 删除头节点
        if index == 0:
            self._head = self._head.next
            return True
        current = self._head
        # 和上述逻辑相同，此处需要找到index的前一个Node节点
        while current and index > 1:
            current, index = current.next, index - 1
        if current is None or current.next is None:
            # 越界
            return False
        if current.next == self._tail:
            self._tail = current
        current.next = current.next.next
        return True
    
    def delete_by_value(self, value: object) -> bool:
        if value is None:
            # 异常验证
            return False
        # 排除删除头节点
        if self._head.value == value:
            self._head = self._head.next
            return True
        
        # 同样是需要找到前一个节点，因此需要一个前置指针
        pre = self._head
        while pre.next and pre.next.value != value:
            pre = pre.next
        if pre.next is None:
            # 越界
            return False
        if pre.next == self._tail:
            self._tail = pre
        pre.next = pre.next.next
        return True

    def reverse(self) -> Node:
        if self._head is None:
            return None
        pre, current = None, self._head
        while current:
            current.next, pre, current = pre, current, current.next
        return pre

    def find_middle_node(self) -> Node:
        # 寻找中间节点
        # 解法：和求解环相同，使用快慢指针，步长一个是1一个是2，当fast指针运行到终点时，慢指针即为中间节点
        slow, fast = self._head, self._head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


    def print(self):
        current, printStr = self._head.next, '%s'%(str(self._head.value))
        while current:
            printStr += ' --> %s'%(str(current.value))
            current = current.next
        print('[%s --> None]'%printStr)


# Testcase
if __name__ == "__main__":
    node5 = Node(5)
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)

    print('初始化：')

    linkedList = LinkedList()
    linkedList.insert(node1)
    linkedList.insert(node2)
    linkedList.insert(node3)
    linkedList.insert(node5)

    print('在index == 3 的地方插入node4之后：')

    node4 = Node(4)
    linkedList.insert_by_index(node4, 3)
    linkedList.print()

    print('删除node3之后：')

    linkedList.delete_by_index(2)
    linkedList.print()

    print('找到node2：')
    linkedList.find_by_value(2).print()

    print('找到尾：')
    linkedList.find_tail().print()

    print('获取中间节点：')
    linkedList.find_middle_node().print()
    
    print('通过value删除：')
    linkedList.print()
    linkedList.delete_by_value(1)
    linkedList.print()

    print('获取反转：')
    linkedList.reverse().print()