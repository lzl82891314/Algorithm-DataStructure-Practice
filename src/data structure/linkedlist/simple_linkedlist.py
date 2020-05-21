# 自定义一个简单链表链表结构

class LinkedList(object):
    def __init__(self, value: object, next = None):
        self.value = value
        self.next = next

    def find_tail(self):
        if self.next is None:
            return self
        current = self.next
        while current.next:
            current = current.next
        return current
    
    def find_by_index(self, index: int = 0):
        if index == 0:
            return self
        current = self
        while current and index > 1:
            current, index = current.next, index - 1
        return current
        

    def find_by_value(self, value: object):
        current = self
        while current and current.value != value:
            current = current.next
        return current
    
    def insert_by_index(self, node, index: int = 0) -> bool:
        if node is None:
            return False
        if index == 0:
            # 插入头部
            node.next = self
            self = node
            return True
        current = self.find_by_index(index)
        if current is None:
            return False
        node.next, current.next = current.next, node
        return True
    
    def delete_by_index(self, index: int = 0) -> bool:
        if index == 0:
            self = self.next
            return True
        current = self.find_by_index(index)
        if not current or not current.next:
            return False
        current.next = current.next.next
        return True
    
    def delete_by_value(self, value: object) -> bool:
        if not value:
            return False
        if self.value == value:
            self.next, self = None, self.next
            return True
        current = self
        while current.next and current.next.value != value:
            current = current.next
        if not current.next:
            return False
        current.next = current.next.next
        return True

    def reverse(self):
        if self.next is None:
            return self
        pre, current = None, self
        while current:
            current.next, pre, current = pre, current, current.next
        return pre

    def find_middle_node(self):
        # 寻找中间节点
        # 解法：和求解环相同，使用快慢指针，步长一个是1一个是2，当fast指针运行到终点时，慢指针即为中间节点
        slow, fast = self, self
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


    def print(self):
        current, printStr = self.next, '%s'%(str(self.value))
        while current:
            printStr += ' --> %s'%(str(current.value))
            current = current.next
        print('[%s --> None]'%printStr)


# Testcase
if __name__ == "__main__":
    node5 = LinkedList(5, None)
    node3 = LinkedList(3, node5)
    node2 = LinkedList(2, node3)
    node1 = LinkedList(1, node2)

    print('初始化：')

    node1.print()

    print('在index == 3 的地方插入node4之后：')

    node4 = LinkedList(4, None)
    node1.insert_by_index(node4, 3)
    node1.print()

    print('删除node3之后：')

    node1.delete_by_index(2)
    node1.print()

    print('找到node2：')
    node1.find_by_value(2).print()

    print('找到尾：')
    node1.find_tail().print()

    print('获取中间节点：')
    node1.find_middle_node().print()
    
    print('通过value删除：')
    node1.print()
    node1.delete_by_value(1)
    node1.print()
    node1.delete_by_value(1)

    print('反转后：')
    node1.reverse().print()