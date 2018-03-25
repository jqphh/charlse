import urllib
import urllib2
import cookielib
import re


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


if __name__ == '__main__':
    #my_http("http://passport.csdn.net/account/login", {'username': 'jqphh@163.com', 'password': '002318304'})
    content = my_http('https://jx3.xoyo.com/index')
    if content is not None:
        try:
            reg = r'src="(.+?\.jpg)"'
            imgre = re.compile(reg)
            imglist = re.findall(imgre, content)

            x = 0

            for imgurl in imglist:
                print imgurl
                #urllib.urlretrieve(imgurl, 'D:\Work\py\%s.jpg' % x)
                x += 1
        except Exception, e:
            print e
