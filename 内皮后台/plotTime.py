
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 16:01:27 2017

@author: zfl
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as line

fig = plt.figure()
ax = plt.axes(xlim=(0,10), ylim=(0,1))
linem = line.Line2D([],[])

def init():
    ax.add_line(linem)
    return linem,

def update(i):
    linem.set_xdata(np.arange(0,10,1))
    linem.set_ydata(np.random.rand(10))
    return linem,

fig.show()

ani = animation.FuncAnimation(fig, update,
                              init_func=init,
                              frames=1,
                              interval=1,
                              blit=True)

raw_input("wait")
 