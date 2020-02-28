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
    # 输入url，请求参数
    request_url = None
    request_param = None

    def __init__(self, url, param=None, target=None, target_path=None, ui_handle=None):
        self.request_url = url
        self.request_param = param
        self.target = target
        self.target_path = target_path
        self.ui_handle = ui_handle

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

    @classmethod
    def super_http_with_cookie(cls):
        print(cls.request_url)

    def super_http_download_img(self, path):
        http = self.request_url.split(':')
        html_content = self.super_http_post()
        if html_content is None:
            return -1

        img_reg = r'((http.:)?//.+\.(jpg|png|jpeg))'
        css_reg = r'((http.:)?//.+\.css)'

        # 1.search img in web content
        img_re = re.compile(img_reg)
        img_list = img_re.findall(html_content)
        for img_info in img_list:
            if 'http' in img_info[1]:
                img_url = img_info[0]
            else:
                img_url = http[0] + ':' + img_info[0]

            file_name = '%s\%s.%s' % (path, get_time_stamp(), img_info[2])
            print(img_url + ':' + file_name)

            # download img
            # urllib.urlretrieve(img_url, file_name)

        # 2.search css in web content
        css_re = re.compile(css_reg)
        css_list = css_re.findall(html_content)
        for css_info in css_list:
            # print css_info
            if 'http' in css_info[1]:
                css_url = css_info[0]
            else:
                css_url = http[0] + ':' + css_info[0]

            print(css_url)
            self.request_url = css_url
            self.super_http_download_img(path)

        return 0

