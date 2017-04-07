
#### opening the eletrophysiology file 
import csv
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
data = genfromtxt('C:\\Users\\sbmiller\\Documents\\Workspace\\Python\\Data.csv', delimiter=',')
TimeArray = []
temp = []
Datatemp = []
SectionArray = []
count = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        if(y == 0):
            TimeArray.append(data[x][0])
        if(y == 1):
            CurrentArray.append(data[x][1])         
plt.plot(TimeArray,CurrentArray,'r',linewidth=2.0)
plt.ylabel('Current')
plt.xlabel('Time')
plt.show()