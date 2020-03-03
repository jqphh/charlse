# _*_ coding:utf-8 _*_

import threading
import time


class jStoppableThread (threading.Thread):
    """
    This class is used to create a stoppable thread, before use this class, mast rewrite run function
    """
    def __init__(self):
        super().__init__()
        self.stop_flag = False

    def stop(self):
        self.stop_flag = True

    def is_stopped(self):
        return self.stop_flag

    def run(self):
        print(time.ctime(time.time()) + " Start thread")
        print(time.ctime(time.time()) + " End thread")
