# Basic Code which uses more CPUs and basically keep polling. Disadvantage of it is that the thisr thread might get triggered 100 times before first threads acquires lock. 
# Non effiicent but working solution
import threading 

class Foo:
    def __init__(self):
        self.lock = threading.Lock()
        self.f = False
        self.s = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        run = True
        while run:
            with self.lock:
                self.f = True
                printFirst()
                run = False

    def second(self, printSecond: 'Callable[[], None]') -> None:
        run = True
        while run:
            with self.lock:
                if self.f:
                    self.s = True
                    printSecond()
                    run = False
    

    def third(self, printThird: 'Callable[[], None]') -> None:
        run = True
        while run:
            with self.lock:
                if self.f and self.s:
                    printThird()
                    run = False
        
