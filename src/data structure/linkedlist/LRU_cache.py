# 使用简单链表实现一个LRU缓存逻辑
# LRU就是最近最少使用缓存
# 设计方法：使用简单链表，当数据进入时判断是否在链表中，如果在则直接返回并且将其移动至尾节点
# 如果不在则插入到链表尾指针，当空间满了删除头指针
# 判存在逻辑可以使用hash表实现优化时间复杂度

from simple_linkedlist import LinkedList
from simple_linkedlist import Node

class LRU_Cache():
    def __init__(self, capecity: int = 10):
        self._capecity = capecity
        self._cache = LinkedList()
        self._contains = 0
        self._dict = dict()

    def set(self, key: str, value: object) -> bool:
        if value is None:
            return False
        
        if key in self._dict:
            # 说明已经存在了对应的缓存值，需要将链表中的对应缓存放入链表尾指针
            self._cache.move_to_tail({ "key": key, "value": value })
            return True
        
        # 说明不存在需要插入
        if self._contains == self._capecity:
            # 内存满了，需要将头节点删除
            head = self._cache.find_by_index(0)
            self._cache.delete_by_index(0)
            # 哈希表也需要删除
            self._dict.pop(head.value['key'])
        self._cache.insert(Node({ "key": key, "value": value }))
        self._contains += 1
        self._dict[key] = value
        return True
    
    def get(self, key: str) -> object:
        # 不存在直接返回None
        value = self._dict[key]
        if not value:
            return None
        # 存在则需要把对应的Node移到链表尾指针
        self._cache.move_to_tail({ "key": key, "value": value })
        return value
    
    def show(self):
        print('cache中的数据为：')
        self._cache.print()
        print('哈希表中的数据为：')
        dictStr = ''
        for index, key in enumerate(self._dict):
            dictStr += '{ key=%s, value=%s }, '%(key, self._dict[key])
        print('[%s]'%(dictStr.rstrip(', ')))
        print('------------------------------------------------------------------')

if __name__ == "__main__":
    cache = LRU_Cache(5)
    cache.set("node1", 1)
    cache.set("node2", 2)
    cache.set("node3", 3)
    cache.set("node4", 4)
    cache.set("node5", 5)
    print('存满缓存后：')
    cache.show()

    temp = cache.get("node3")
    print('读取node3后：')
    cache.show()

    cache.set("node6", 6)
    print('存入node6后：')
    cache.show()

