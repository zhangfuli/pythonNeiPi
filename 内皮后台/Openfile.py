# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:54:11 2017

@author: Administrator
"""
import scipy.signal
#from scipy import signal
import numpy as np 
from matplotlib import pyplot as plt 

'例程3  滤波器'
def butter_lowpass(freqcut, fs, order=3):
    nyq = 0.5 * fs
    freq = freqcut / nyq
    b, a = scipy.signal.butter(order, freq, btype='low')
    return b, a
    
def butter_highpass(freqcut, fs, order=3):
    nyq = 0.5 * fs
    freq = freqcut / nyq
    b, a = scipy.signal.butter(order, freq, btype='high')
    return b, a

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = scipy.signal.butter(order, [low, high], btype='band')
    return b, a
    
fs = 20000.0
N = 2000
freq = 1000
freq2 = 100
time = np.linspace(0,float(N)/fs,N)
sine = 0.264*np.sin(2*np.pi*time*freq)      #正弦波
sine2 = 1+0.5*np.sin(2*np.pi*time*freq2)
sig = sine+sine2

b, a = butter_highpass(500, fs, order = 3)  
sig = scipy.signal.filtfilt(b, a, sig)

plt.plot(sig[:1000])
plt.show()



#'例程4  读取文件'
#fname = 'test.csv'   #test.csv放在相同目录下
#data = np.genfromtxt(fname, delimiter= ",")
#x = np.array(data).astype(np.float32).T
#plt.plot(x[:400000])
#plt.show()

