# _*_ coding:utf-8 _*_

from urllib import request
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

    @staticmethod
    def super_http_post(url):
        try:
            # req = request.Request(self.request_url)
            resp = request.urlopen(url)
            #bytes to string
            content = resp.read().decode()
            resp.close()
            return content
        except Exception as e:
            print(e)

    @classmethod
    def super_http_with_cookie(cls):
        print(cls.request_url)

    @staticmethod
    def super_download_img(url, path):
        request.urlretrieve(url, path)

    def super_http_download_img(self, path):
        #print "Visit website %s" % self.request_url

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
        
        return 0

    def super_download_story(self):
        content = httpRequest.super_http_post(self.request_url)
        if content is None:
            return -1

        content_reg = r'<dd><a href="(.*?)" title="(.*?)">(.*?)</a></dd>'
        content_re = re.compile(content_reg)
        story_list = content_re.findall(content)
        for story_info in story_list:
            child_url = self.request_url + '/' + story_info[0]
            httpRequest.download_and_save_file(child_url, story_info[1])

        return 0

    @staticmethod
    def download_and_save_file(url, title):
        print('Downloading ' + title + ':' + url)
        content = httpRequest.super_http_post(url)
        if content is None:
            return -1

        content_reg = r'<div id="content">(.*?)</div>'
        content_re = re.compile(content_reg)
        story_content = content_re.findall(content)
        print(story_content)

        f = open(r'D:\绝世唐门.txt', 'a+')
        f.writelines(title + '\n')
        f.writelines(story_content[0] + '\n')
