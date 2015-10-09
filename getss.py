# -*- coding: utf-8 -*-
__author__ = 'xdc'

import requests
import json

def get_ss(url,filename):
    r =requests.get(url)
    fp=open(filename,'w')
    data =r.json()

    #print data
    data["server"]=data.pop("ip")
    data["server_port"]=data.pop("port")
    data["method"]=data.pop('method')
    data['local_address']='127.0.0.1'
    data['timeout']=600
    data['local_port']='1080'
    #data["remarks"]="CN_SS"
    json.dump(data,fp,skipkeys=True)
    fp.close()

if __name__ =='__main__':
    get_ss("http://qr.thankgfw.ml/?type=json","config.json")
