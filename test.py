# _*_ coding:utf-8 _*_

from jThread import jThread
from httpRequest import httpRequest
import time
import socket
from jMysql import jMysql


def time_thread(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print(name + ' ' + time.ctime(time.time()))
        count += 1


def tcp_test(host):
    while True:
        time.sleep(5)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                print('connect ' + host[0])
                sock.connect(host)
                str = '{\'id\':1}'
                sock.send(str.encode('utf-8'))
                re = sock.recv(1024)
        except Exception as e:
            print(e)


def download_story():
    # story = httpRequest('https://www.biquge.info/0_580/', target='绝世唐门', target_path='D:\\story')
    story = httpRequest('http://www.xbiquge.la/5/5651/', target='朱雀记', target_path='D:\\story')
    story.download_story()


def test_mysql():
    mysql = {
        'host': '47.106.37.46',
        'user': 'root',
        'passwd': 'Lichenxin1!',
        'db': 'weibo'
    }
    mysql_client = jMysql(host=mysql['host'], user=mysql['user'], passwd=mysql['passwd'], db=mysql['db'])
    result = mysql_client.execute_sql('SHOW TABLES')
    if result is not None:
        for x in result:
            print(x)

    result = mysql_client.execute_sql('SELECT * FROM login_info')
    if result is not None:
        for x in result:
            print(x)


if __name__ == '__main__':
    # download_story()
    # test_mysql()
    # tcp_test(('54.222.181.181', 8083))
    thread1 = jThread('a', time_thread, ('a', 1))
    thread2 = jThread('b', time_thread, ('b', 2))
    thread1.start()
    thread2.start()


