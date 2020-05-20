# Array类型数据结构的自定义实现
# 主要包括增删改查等操作

class MyArray():
    def __init__(self, capacity: int = 10):
        # 使用基础的数据类型数组完成自定义Array的数据层功能
        self._data = []
        # 数组没有动态分配空间的概念，这个概念是List的，因此此字段只做展示使用
        self._capacity = capacity

    def __getitem__(self, index: int) -> object:
        return self._data[index]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for i in range(0, self._capacity):
            try:
                yield self._data[i]
            except:
                yield None
        
    def insert(self, value: object) -> bool:
        if len(self._data) >= self._capacity:
            # 当空间满了直接返回错误
            return False
        self._data.append(value)
    
    def delete(self, index: int) -> bool:
        # 此处应该用到异常处理，自己实现的代码中没有使用异常处理
        try:
            self._data.pop(index)
            return True
        # 这里只捕获了数组越界的问题
        except IndexError:
            return False
        
    def update(self, index: int, value: object) -> bool:
        if self.delete(index):
            self._data[index] = value
            return True
        return False
        
    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None
    
    def print(self):
        printStr = str()
        for item in self:
            printStr += '%s, '%(str(item))
        print('[%s]'%(printStr.rstrip(', ')))

if __name__ == "__main__":
    myArr = MyArray()
    myArr.insert(1)
    myArr.insert(2)
    myArr.insert(3)
    myArr.insert(4)
    myArr.insert(5)

    myArr.print()