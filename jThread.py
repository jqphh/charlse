# _*_ coding:utf-8 _*_

import threading
import time


class jThread (threading.Thread):
    def __init__(self, thread_name, thread_func, thread_arg):
        threading.Thread.__init__(self)
        self.threadName = thread_name
        self.threadFunc = thread_func
        self.threadArg = thread_arg

    def run(self):
        print(time.ctime(time.time()) + " Start thread: " + self.threadName)
        self.threadFunc(*self.threadArg)
        print(time.ctime(time.time()) + " End thread: " + self.threadName)
