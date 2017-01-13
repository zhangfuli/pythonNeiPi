# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:46:28 2017

@author: Administrator
"""
from functools import wraps
import json
from flask import Flask
from flask import make_response
import numpy as np 
from matplotlib import pyplot as plt 
#from scipy.stats import gmean


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] ="http://localhost:4000"
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        rst.headers['Access-Control-Allow-Credentials'] = 'true'
        allow_headers = "Referer,Accept,Origin,User-Agent,x-requested-with,content-type"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

app = Flask(__name__)

# 生成正弦波
fs = 20000.0
N = 2000
freq = 1000
freq2 = 100
time = np.linspace(0,float(N)/fs,N)

sine = 0.264*np.sin(2*np.pi*time*freq)      #正弦波

plt.plot(sine)
plt.show()

plt.plot(sine[:100])  #查看信号段
plt.show()

t = plt.psd(sine)

#list转JSON
def listToJson(oldlist):
    newlist = []
    listkey = []
    count = 0
    for i in oldlist:
        newlist.append(i)
        countstr = str(count)
        listkey.append(countstr)
        count = count + 1
    dic = dict(zip(listkey,newlist))
    return json.dumps(dic)

yAxis = listToJson(t[0])
xAxis = listToJson(t[1])


#返回Y坐标
@app.route('/yAxis',methods = ['GET'])
@allow_cross_domain
def giveYaxis():
    return yAxis

#返回X坐标
@app.route('/xAxis',methods = ['GET'])
@allow_cross_domain
def giveXaxis():
    return xAxis
    
#@app.route('/CI',methods = ['GET'])
#@allow_cross_domain
#def giveCI():
#    return CI    


if __name__ == '__main__':
    app.run()