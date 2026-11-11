import threading 

class Foo:
    def __init__(self):
        self.condition1 = threading.Condition()
        self.condition2 = threading.Condition()
        self.f = False
        self.s = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.condition1:
            self.f = True
            printFirst()
            self.condition1.notify()
            
            

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition1:
            while not self.f:
                self.condition1.wait()
            printSecond()
        
        with self.condition2:
            self.s = True
            self.condition2.notify()
    

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.condition2:
            while not self.s:
                self.condition2.wait()
            printThird()
        
