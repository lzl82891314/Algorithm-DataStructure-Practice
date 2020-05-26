class MyQueue:

    def __init__(self):
        self._data = []
        self._stack = []
        

    def push(self, x: int) -> None:
        while self._data:
            self._stack.append(self._data.pop())
        self._stack.append(x)
        while self._stack:
            self._data.append(self._stack.pop())
        

    def pop(self) -> int:
        return self._data.pop()
        

    def peek(self) -> int:
        item = self._data.pop()
        self._data.append(item)
        return item
        

    def empty(self) -> bool:
        return len(self._data) == 0