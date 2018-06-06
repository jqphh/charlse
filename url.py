import urllib
import urllib2
import cookielib
import re
import time


def my_http(url, param=None):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

    try:
        if param is not None:
            data = urllib.urlencode(param)
        else:
            data = None
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return response.read()
    except Exception, e:
        print e
        return None


def my_http_get_cookie(url, param):
    filename = 'D:\Work\py\csdn_cookie.txt'
    try:
        cookie = cookielib.MozillaCookieJar(filename)
        handle = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handle)
        data = urllib.urlencode(param)
        opener.open(url, data)
        cookie.save(ignore_discard=True, ignore_expires=True)
        return True
    except Exception, e:
        print e
        return False


def my_http_with_cookie(url, param):
    filename = 'D:\Work\py\csdn_cookie.txt'
    try:
        cookie = cookielib.MozillaCookieJar(filename)
        handle = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handle)
        data = urllib.urlencode({
            'username': 'jqphh@163.com',
            'password': '002318304'
        })
        login_url = 'https://passport.csdn.net/account/login'
        opener.open(login_url, data)
        cookie.save(ignore_discard=True, ignore_expires=True)

        grade_url = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
        result = opener.open(grade_url)
        print result.read()
    except Exception, e:
        print e


# my_http("http://passport.csdn.net/account/login", {'username': 'jqphh@163.com', 'password': '002318304'})


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d-%H-%M-%S", local_time)
    data_secs = (ct - long(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def download_img(url):
    if url is None:
        return -1

    print "Visit website %s" % url

    http = url.split(':')
    html_content = my_http(url)
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

        file_name = 'D:\py\%s.%s' % (get_time_stamp(), img_info[2])
        print img_url, file_name

        # download img
        urllib.urlretrieve(img_url, file_name)

    # 2.search css in web content
    css_re = re.compile(css_reg)
    css_list = re.findall(css_re, html_content)
    for css_info in css_list:
        # print css_info
        if 'http' in css_info[1]:
            css_url = css_info[0]
        else:
            css_url = http[0] + ':' + css_info[0]

        file_name = 'D:\py\%s.%s' % (get_time_stamp(), img_info[2])
        print img_url, file_name

        download_img(css_url)


if __name__ == '__main__':
    # download_img('https://n.163.com/#job')
    download_img('https://jx3.xoyo.com/index')
    # download_img('http://zmq.163.com')
