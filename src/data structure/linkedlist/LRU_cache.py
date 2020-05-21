# 使用简单链表实现一个LRU缓存逻辑
# LRU就是最近最少使用缓存
# 设计方法：使用简单链表，当数据进入时判断是否在链表中，如果在则直接返回并且将其重新插入链表表头
# 如果不存在则插入头指针。如果缓存满了，则删除尾指针
# 判存在逻辑可以使用hash表实现优化时间

from simple_linkedlist import LinkedList

class LRU_Cache():
    def __init__(self, capecity: int = 10):
        self._capecity = capecity
        self._cache = LinkedList()  # 头指针，作为要给哨兵，内部无数据
        self._contains = 0
        self._dict = dict()
