#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import httplib
import urllib
import simplejson as json

translate = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def http_post(host, port, uri, content):
    try:
        client = httplib.HTTPConnection(host, port)
        client.request(method="POST", url=uri, body=content)
        response = client.getresponse()
        res = response.read()
        print res
    except Exception, e:
        print e
    finally:
        if client is not None:
            client.close()

def http_get(url):
    try:

    except Exception, e:
        print e
    finally:


