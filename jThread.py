# _*_ coding:utf-8 _*_

import threading
import time

class jThread (threading.Thread):
    def __init__(self, threadName, threadFunc, threadArg):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.threadFunc = threadFunc
        self.threadArg = threadArg

    def run(self):
        print(time.ctime(time.time()) + " Start thread: " + self.name)
        self.threadFunc(self.threadName, self.threadArg)
        print(time.ctime(time.time()) + " End thread: " + self.name)
