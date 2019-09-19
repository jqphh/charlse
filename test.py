# _*_ coding:utf-8 _*_

from jThread import jThread
from httpRequest import httpRequest
import time
import socket


def time_thread(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print(name + ' ' + time.ctime(time.time()))
        count += 1


def tcp_test(host):
    while True:
        time.sleep(15)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('connect ' + host[0])
            sock.connect(host)
            sock.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    story = httpRequest('https://www.biquge.info/0_580/', target='绝世唐门', target_path='D:\\story')
    story.download_story()

    #url1 = 'http://device.chiq-cloud.com:8080/cdc/device/register'
    #param1 = '{"system":{"ipp":"3.0","key":"key3.0"},"request":{"devlist":[{"devid":"MY2w3DRvmacaT17070300818","sn":"MY2w3DRvmacaT17070300818","productid":"SLIFE_GW0001-7406593c56","swver":"2.6.099","mac":"A2:B2:CD:EE:F2:A3"}]}}'
    #ipp = httpRequest.super_http_post(url1, param1)