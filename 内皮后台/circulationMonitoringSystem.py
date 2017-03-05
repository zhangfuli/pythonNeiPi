# -*- coding: utf-8 -*-

import numpy as np 
from matplotlib import pyplot as plt 
from scipy.stats import gmean
import scipy.signal
import serial  
from time import sleep  
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
    
# 带通滤波器
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = scipy.signal.butter(order, [low, high], btype='band')
    return b, a
    
#求psd
def PSD(signal):
    psd = plt.psd(signal) #精度精确到小数点后3位
    # psd[0] 纵坐标  psd[1] 横坐标
    return psd[0]
    
def SFM(psd):
    psd = psd * (10^6)
    arithmetic = np.average(psd)  # 算数平均值
    geometric = gmean(psd)  # 几何平均数
    # print gmean([1,2])
    SFM = geometric/arithmetic
    return SFM
    
#生成随机数
plt.xlim(0,20)
plt.ylim(0,1)
plt.ion()
y = []
i = 0  #用于横坐标的变化
t = 0   #用于显示一组数据
while True:
    temp = np.random.random()
    i += 1
    y.append(temp)
    if i>=100:
        if t == 0:
            print "normalization"
            print normalization(y)
            #滤波 低通0.6高通25     
            b, a = butter_bandpass(0.6,25,20000.0,order = 5)
            sig = scipy.signal.filtfilt(b, a,normalization(y))
            # 先求psd再求SFM    CI=1-SFM
            print "SFM" 
            print SFM(PSD(sig))
            sfm = SFM(PSD(sig))
            #求取CI
            print "CI"
            print 1-sfm
        t=t+1        
    if i>20:
    	plt.xlim(i-20,i)
    plt.plot(y)
    plt.pause(0.1)


#ser = serial.Serial('COM4', 115200, timeout=0.5)
#plt.ion()  #  开启matplotlib的交互模式
#plt.xlim(0,50)  #首先得设置一个x轴的区间 这个是必须的
#plt.ylim(-19.58,19.58) # y轴区间 
#acc_speed = []
#i = 0  #计数。然x轴能到了初始状态的最大值能进行改变
#while True:
#	ser.flushInput()#清除缓冲区
#	temp =ser.read(8) #读取传来的6个字符
#	acc_speed.append(temp)  #存入list里面
#	i += 1
#	if i>50:    #初始状态x轴最大为50
#		plt.xlim(i-50,i) #  如果当前坐标x已经超过了50，将x的轴的范围右移。
#	plt.plot(y) #将list传入plot画图
#	plt.pause(0.01) # 这个为停顿0.01s，能得到产生实时的效果