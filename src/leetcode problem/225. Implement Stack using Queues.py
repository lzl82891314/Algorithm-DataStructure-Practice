from queue import Queue

class MyStack:

    def __init__(self):
        self._data = Queue()
        self._queue = Queue()

    def push(self, x: int) -> None:
        self._queue.put(x)
        while not self._data.empty():
            self._queue.put(self._data.get())
        
        # swap
        self.tempQueue = self._data
        self._data = self._queue
        self._queue = self.tempQueue
               

    def pop(self) -> int:
        return self._data.get()
        

    def top(self) -> int:
        return self._data.queue[0]
        

    def empty(self) -> bool:
        return self._data.empty()