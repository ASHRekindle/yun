import requests
import random
import time
import json
import hashlib

class Youdao(object):

    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        return self.ts + str(random.randint(0, 10))

    def get_md5(self,value):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s = "fanyideskweb" + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)

    def get_ts(self):
        t = time.time()
        return str(int(round(t * 1000)))

    def yield_headers(self):
        return {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-25201430@10.169.0.82; JSESSIONID=aaa_9bXnOSg8b_xSdyYfx; OUTFOX_SEARCH_USER_ID_NCOO=901760003.6171594; ___rl__test__cookies=1586761886929',
            'Referer': 'http: // fanyi.youdao.com /',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }

    def yield_form_data(self):
        return {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'cc652a2ad669c22da983a705e3bca726',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.yield_headers())
        content=json.loads(response.text)
        return content ['translateResult'][0][0]['tgt']

if __name__ == '__main__':
    while(True):
        i=input("please input : ")
        youdao=Youdao(i)
        print(youdao.fanyi())
