#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib
import urllib2
import cookielib
import re
import time


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d-%H-%M-%S", local_time)
    data_secs = (ct - long(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp


class HttpRequest:
    # 输入url，请求参数
    request_url = None
    request_param = None

    def __init__(self, url, param=None):
        self.request_url = url
        self.request_param = param

    def super_http(self):
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

        try:
            if self.request_param is not None:
                data = urllib.urlencode(self.request_param)
            else:
                data = None
            request = urllib2.Request(self.request_url, data, headers)
            response = urllib2.urlopen(request)
            return response.read()
        except Exception, e:
            print e
            return None

    def super_http_with_cookie(self):
        pass

    def super_http_download_img(self, path):
        if self.request_url is None or path is None:
            return -1

        print "Visit website %s" % self.request_url

        http = self.request_url.split(':')
        html_content = self.super_http()
        if html_content is None:
            return -2

        img_reg = r'((http.:)?//.+\.(jpg|png|jpeg))'
        css_reg = r'((http.:)?//.+\.css)'

        # 1.search img in web content
        img_re = re.compile(img_reg)
        img_list = re.findall(img_re, html_content)
        for img_info in img_list:
            # print img_info
            if 'http' in img_info[1]:
                img_url = img_info[0]
            else:
                img_url = http[0] + ':' + img_info[0]

            file_name = '%s\%s.%s' % (path, get_time_stamp(), img_info[2])
            print img_url, file_name

            # download img
            urllib.urlretrieve(img_url, file_name)

        # 2.search css in web content
        """css_re = re.compile(css_reg)
        css_list = re.findall(css_re, html_content)
        for css_info in css_list:
            # print css_info
            if 'http' in css_info[1]:
                css_url = css_info[0]
            else:
                css_url = http[0] + ':' + css_info[0]

            file_name = 'D:\py\%s.%s' % (get_time_stamp(), img_info[2])
            print img_url, file_name

            download_img(css_url)"""
