#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import thread
import time
from HttpRequest import HttpRequest
import socket
import binascii

def time_thread(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print "%s: %s" % (name, time.ctime(time.time()))
        count += 1


if __name__ == '__main__':
    '''try:
        thread.start_new_thread(time_thread, ("Thread-1", 2))
        thread.start_new_thread(time_thread, ("Thread-2", 4))
    except Exception, e:
        print e

    while 1:
        pass'''

    #client = HttpRequest(url='https://n.163.com/index.html')
    #client.super_http_download_img('D:\py')

    fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fd.bind(('0.0.0.0', 23456))
    while True:
        data, addr = fd.recvfrom(1024)
        print 'Received from %s:%s' % addr

        print 'Header  :%x %x' % (int(data[0].encode('hex'), 16), int(data[1].encode('hex'), 16))
        print 'Type1   :%x' % int(data[2].encode('hex'), 16)
        print 'Type2   :%x' % int(data[3].encode('hex'), 16)
        print 'Cmd     :%x' % int(data[4].encode('hex'), 16)
        print 'Cmd len :%x' % int(data[5].encode('hex'), 16)
        print 'Cmd data:'

        val = int(data[6].encode('hex'), 16)
        sweep_floor = val & 0x01
        back_charge = (val & 0x02) >> 1
        wind = (val & 0x18) >> 3
        full_power = (val & 0x20) >> 5

        val = int(data[7].encode('hex'), 16)
        mode = val & 0x07
        ahead = (val & 0x18) >> 3
        left = (val & 0x60) >> 5

        appoint0 = [1, 1, 1, 1]
        appoint1 = [1, 1, 1, 1]
        appoint2 = [1, 1, 1, 1]
        appoint3 = [1, 1, 1, 1]
        appoint4 = [1, 1, 1, 1]

        val = int(data[8].encode('hex'), 16)
        charging = val & 0x03
        appoint0[3] = (val & 0x04) >> 2
        appoint1[3] = (val & 0x08) >> 3
        appoint2[3] = (val & 0x10) >> 4
        appoint3[3] = (val & 0x20) >> 5
        appoint4[3] = (val & 0x40) >> 6

        appoint = int(data[9].encode('hex'), 16)
        electricity = int(data[10].encode('hex'), 16)
        appoint0[0] = int(data[11].encode('hex'), 16)
        appoint0[1] = int(data[12].encode('hex'), 16)
        appoint0[2] = int(data[13].encode('hex'), 16)
        appoint1[0] = int(data[14].encode('hex'), 16)
        appoint1[1] = int(data[15].encode('hex'), 16)
        appoint1[2] = int(data[16].encode('hex'), 16)
        appoint2[0] = int(data[17].encode('hex'), 16)
        appoint2[1] = int(data[18].encode('hex'), 16)
        appoint2[2] = int(data[19].encode('hex'), 16)
        appoint3[0] = int(data[20].encode('hex'), 16)
        appoint3[1] = int(data[21].encode('hex'), 16)
        appoint3[2] = int(data[22].encode('hex'), 16)
        appoint4[0] = int(data[23].encode('hex'), 16)
        appoint4[1] = int(data[24].encode('hex'), 16)
        appoint4[2] = int(data[25].encode('hex'), 16)
        alarm = int(data[26].encode('hex'), 16)

        print "======================================================="
        print "mode        : %d" % mode
        print "sweepfloor  : %d" % sweep_floor
        print "backcharge  : %d" % back_charge
        print "wind        : %d" % wind
        print "electricity : %d" % electricity
        print "ahead       : %d" % ahead
        print "left        : %d" % left
        print "fullpower   : %d" % full_power
        print "charging    : %d" % charging
        print "appoint     : %d" % appoint
        print "alarm       : %d" % alarm
        print "appoint0    : %x-%d-%d-%d" % (appoint0[0], appoint0[1], appoint0[2], appoint0[3])
        print "appoint1    : %x-%d-%d-%d" % (appoint1[0], appoint1[1], appoint1[2], appoint1[3])
        print "appoint2    : %x-%d-%d-%d" % (appoint2[0], appoint2[1], appoint2[2], appoint2[3])
        print "appoint3    : %x-%d-%d-%d" % (appoint3[0], appoint3[1], appoint3[2], appoint3[3])
        print "appoint4    : %x-%d-%d-%d" % (appoint4[0], appoint4[1], appoint4[2], appoint4[3])
        print "======================================================="
