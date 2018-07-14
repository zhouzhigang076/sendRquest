#!/usr/bin/python2.7
# coding=utf-8

import json
from Common import get,post


def GetRequest(url,repeat=0):
    param = {'Type':1,'HotelIds':0,'Status':0}
    reqJson = get(url, param)
    try:
        reqArr = json.loads(reqJson.text)
        # if reqArr['status']['code'] in [200,'200']:
        #     return reqArr['data']
        return reqArr
    except:
        repeat = repeat + 1
        if 3 <= repeat:
            return False
        else:
            GetRequest(url, repeat)


if __name__ == "__main__":
    url="http://127.0.0.1:9090/v1/bw_score/hotel_list"
    res = GetRequest(url)
    print res
    print res

