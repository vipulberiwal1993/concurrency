import threading 
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = deque()
        self.capacity = capacity
        self.condition = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.condition:
            while len(self.q) == self.capacity:
                self.condition.wait()
            self.q.append(element)
            self.condition.notify()

    def dequeue(self) -> int:
        with self.condition:
            while len(self.q) == 0:
                self.condition.wait()
            value = self.q.popleft()
            self.condition.notify()
            return value

    def size(self) -> int:
        with self.condition:
            return len(self.q)
        
