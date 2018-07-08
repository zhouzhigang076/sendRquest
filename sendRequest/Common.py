#!/usr/bin/python2.7
# coding=utf-8

import requests

def get(url,param):
    result = []
    headers=""
    try:
        result = requests.get(url, params=param, headers=headers, verify=False)
        return result
    except Exception as e:
        return result

def post(url, param):
    result = []
    headers={
    # "User-Name": "bw_score",
    "User-Name": "bw_aladdin_test",
    "Accept-Encoding": "gzip,deflate",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0(WindowsNT6.1;WOW64;rv:34.0)Gecko/20100101Firefox/34.0",
    "Access-Token": "492f7088c972dd946ae229408c0ff5e7"
}
    try:
        result = requests.post(url, params=param, headers=headers, verify=False)
        return result
    except Exception as e:
        return result