#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import thread
import time


def time_thread(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print "%s: %s" % (name, time.ctime(time.time()))
        count += 1


if __name__ == '__main__':
    try:
        thread.start_new_thread(time_thread, ("Thread-1", 2))
        thread.start_new_thread(time_thread, ("Thread-2", 4))
    except Exception, e:
        print e

    while 1:
        pass
