# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 17:00:44 2017

@author: zfl
"""
import time
from pymongo import *

# 获取当前时间
localtime = time.asctime( time.localtime(time.time()) )

#链接数据库
client = MongoClient() 
client = MongoClient("mongodb://localhost:27017/")

db = client.test
collection = db.test_collection

mydict = {"name":"test","time":localtime,"CI":18}
collection.insert_one(mydict)


