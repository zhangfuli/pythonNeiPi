# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:46:28 2017

@author: Administrator
"""

import numpy as np 
from matplotlib import pyplot as plt 
from scipy.stats import gmean
#例程1 生成正弦波
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

#归一化
def normalization(sine):
    array = np.array(sine)
    arrayMax = -np.sort(-array, axis=0)
    maxNum = arrayMax[0]
    arrayMin = np.sort(array,axis = 0)
    minNum = arrayMin[0]    
    plt.plot((array-minNum)/(maxNum-minNum))
    newArray = (array-minNum)/(maxNum-minNum)
    return newArray
    
def SFM(psd):
    psd = psd * (10^6)
    arithmetic = np.average(psd)  # 算数平均值
    geometric = gmean(psd)  # 几何平均数
    # print gmean([1,2])
    SFM = geometric/arithmetic
    return SFM
    
def PSD(signal):
    psd = plt.psd(signal) #精度精确到小数点后3位
    # psd[0] 纵坐标  psd[1] 横坐标
    print psd[0]

PSD(sine)









