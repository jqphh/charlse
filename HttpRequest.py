# _*_ coding:utf-8 _*_

import urllib.request
#import cookielib
import re
import ssl
import time


def get_time_stamp():
    return time.ctime(time.time())


class httpRequest:
    # 输入url，请求参数
    request_url = None
    request_param = None

    def __init__(self, url, param=None):
        self.request_url = url
        self.request_param = param

    def super_http_post(self):
        try:
            if self.request_param is not None:
                self.request_param = urllib.parse.urlencode(self.request_param)

            req = urllib.request.Request(self.request_url)
            resp = urllib.request.urlopen(req)
            #bytes to string
            return resp.read().decode()
        except Exception as e:
            print(e)

    def super_http_with_cookie(self):
        pass

    def super_http_download_img(self, path):
        #print "Visit website %s" % self.request_url

        http = self.request_url.split(':')
        html_content = self.super_http_post()
        if html_content is None:
            return -2

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
            #urllib.urlretrieve(img_url, file_name)

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
