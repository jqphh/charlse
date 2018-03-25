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


if __name__ == '__main__':
    val = "{\"system\":{\"ipp\":\"3.0\",\"key\":\"key3.0\"},\"request\":{\"kid\":\"CH_SPEAKER_001\"}}"
    ret = json.loads(val)
    print "%s\n%s" % (ret['system'], ret['request'])
    http_post("device.chiq-cloud.com", 8080, "/cdc/device/systime", "{}")

    data = {}
    data['i'] = '星期天'
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1515930176349'
    data['sign'] = 'e93195638d3e86894d340ac2baa9b619'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'
    param = urllib.urlencode(data)
    http_post('fanyi.youdao.com', None, '/translate_o?smartresult=dict&smartresult=rule', param)
