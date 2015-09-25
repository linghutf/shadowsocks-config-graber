# -*- coding: utf-8 -*-
__author__ = 'xdc'

import requests
from bs4 import BeautifulSoup as bs
import re
import json
#from threading import Timer
#import time

class NetExcetion(Exception):
    def __init__(self,s):
        Exception.__init__(self,s)
        print s

def getssjson(url):
    r=requests.get(url)
    soup = bs(r.content,'lxml')
    ss = soup.find_all('div',attrs={'class':'col-md-6','style':'margin-left:-15px'})
    #ip
    p=re.compile(r'((\w+\.){2}\w+)|((\d{,3}\.){3}(\d{,3}){1})',re.U)
    filename = "myconfig"
    ext = ".json"
    i=1
    for t in ss:
        data=getcontent(t,p)
        write_ss_configfile(data,filename+str(i)+ext)
        i+=1

def isPort(p):
    return p>=0 and p<=65535

def isIpAddr(ip,pattern):
    return pattern.search(ip)

def checkout(rawdata):
    return rawdata[rawdata.find(u":")+1:].strip()

def getcontent(tag,p):
    #hard decode tag
    ip=tag.p.next_sibling
    port=ip.next_sibling
    passwd=port.next_sibling
    encry=passwd.next_sibling

    _ip = checkout(ip.get_text())
    if not isIpAddr(_ip,p):
        raise NetExcetion("Address or Ip error!")

    _port =int(checkout(port.get_text()))
    if not isPort(_port):
        raise NetExcetion("Port is illegal!")

    password = checkout(passwd.get_text())
    _encry = checkout(encry.get_text())

    data={"timeout":600,
          "method":_encry,
          "password":password,
          "server_port":_port,
          "server":_ip}
    return data

def write_ss_configfile(data,filename):
    fp=open(filename,'w')
    json.dump(data,fp)
    fp.close()

if __name__ == '__main__':
    url = "http://kf0.cc"
    getssjson(url)
