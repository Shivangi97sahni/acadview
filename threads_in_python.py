#1
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(5)
        print("I am of", self.h)


thread1 = mythread(20)
thread1.start()


#2
import threading
import time

def loop1_10():
    for i in range(1,11):
        time.sleep(1)
        print(i)

threading.Thread(target=loop1_10).start()


#3
list=["twitter","facebook","instagram","musicaly","like"]
import threading
from threading import Thread
import time
class mylist(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        for i in list:
            print("display list item with a gap of 2 seconds: ",i)
            time.sleep(2)
Thread1=mylist(1)
Thread1.start()


#4
import threading
from threading import Thread
import time,math
class factorial(threading.Thread):
    def __init__(self, fact):
        threading.Thread.__init__(self)
        self.f=fact

    def run(self):
        time.sleep(20)
        print(math.factorial(self.f))

thread1=factorial(4)
thread1.start()






