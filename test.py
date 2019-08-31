# _*_ coding:utf-8 _*_

from jThread import jThread
from httpRequest import httpRequest
import time

def time_thread(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print(name + ' ' + time.ctime(time.time()))
        count += 1


if __name__ == '__main__':
    '''try:
        thread1 = jThread("Thread-1", time_thread, 1)
        thread2 = jThread("Thread-2", time_thread, 1)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    except Exception as e:
        print(e)

    print("exit")'''
    #client = httpRequest(url='https://n.163.com/index.html')
    #client.super_http_download_img('D:\py')
    img = 'https://i.ys7.com/streamer/alarm/url/get?fileId=20190829171859-159723239-1-00000-2-1&deviceSerialNo=159723239&cn=1&isEncrypted=1&ct=1&lc=90&bn=1_hikalarm'
    img_file = 'D:\img.jpg'

    httpRequest.super_http_with_cookie()
    httpRequest.super_download_img(img, img_file)
