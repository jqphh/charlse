# _*_ coding:utf-8 _*_

import urllib.request
from io import BytesIO

from bs4 import BeautifulSoup
import re
import time
import gzip


def get_time_stamp():
    return time.ctime(time.time())


class httpRequest:

    @staticmethod
    def super_download_img(url, path):

        urllib.request.urlretrieve(url, path)

    @staticmethod
    def super_http(url, param=None, param_type='json'):
        header = None
        data = param
        try:
            if param is not None:
                if param_type == 'json':
                    header = {'Content-type': 'application/json'}
                elif param_type == 'form':
                    header = {'Content-type': 'application/from'}
                    data = urllib.parse.urlencode(param).encode('utf-8')
                else:
                    header = {'Content-type': 'application/raw'}
                    data = urllib.parse.urlencode(param).encode('utf-8')

                # string to byte
                # data = bytes(data, 'utf-8')
                data = data.encode('utf-8')
            else:
                pass
        except Exception as e:
            print(e)

        try:
            print('访问' + url)
            if data is not None:
                # 传data参数，通过post方式访问
                req = urllib.request.Request(url, data, header)
            else:
                # 通过get方式访问
                req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)

            # 处理网站gzip压缩流
            encode_type = resp.info().get('Content-Encoding')
            if encode_type == 'gzip':
                content = resp.read()
                buff = BytesIO(content)
                f = gzip.GzipFile(fileobj=buff)
                content = f.read().decode('utf-8')
            else:
                content = resp.read().decode('utf-8')

            resp.close()
            return content
        except Exception as e:
            print(e)


