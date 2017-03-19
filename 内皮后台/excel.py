# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 21:19:27 2017

@author: zfl
"""
import time
import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import mlab as mlab 
from scipy.stats import gmean
import scipy.signal
import xlrd
#归一化
def normalization(sine):
    array = np.array(sine)
    arrayMax = -np.sort(-array, axis=0)
    maxNum = arrayMax[0]
    arrayMin = np.sort(array,axis = 0)
    minNum = arrayMin[0]    
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
    psd =psd *(10^6)
    arithmetic = np.average(psd)  # 算数平均值
    geometric = gmean(psd)  # 几何平均数
    # print gmean([1,2])
    SFM = geometric/arithmetic
    return SFM


#open excel file and get sheet
myBook = xlrd.open_workbook(r'test.xlsx')
mySheet = myBook.sheet_by_index(0)

#get datas
time = mySheet.col(0)
time = [x.value for x in time]
#print time

#drop the 1st line of the data, which is the name of the data.
#b, a = butter_bandpass(0.6,25,150000.0,order = 5)
#sig = scipy.signal.filtfilt(b, a,normalization(time))
sfm = SFM(PSD(normalization(time)))
print 1-sfm